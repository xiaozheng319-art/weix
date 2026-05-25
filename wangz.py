import streamlit as st
import re
import random

# 设置网页基本配置
st.set_page_config(
    page_title="微信小程序全量互动刷题系统",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="expanded"
)


# ==============================================================================
# 🎨 视觉美化 CSS 样式（超级大字号题目、卡片式选项按钮化改造）
# ==============================================================================
def inject_custom_css():
    st.markdown("""
    <style>
    /* 全局背景色调 */
    .stApp {
        background-color: #f7f9fc;
    }

    /* 顶部标题美化 */
    .main-title {
        font-size: 2.5rem !important;
        font-weight: 800 !important;
        color: #07c160;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #666666;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }

    /* 巨型题目展示文本 */
    .big-question-text {
        font-size: 24px !important;
        font-weight: 700 !important;
        color: #111111;
        line-height: 1.6 !important;
        margin-top: 10px;
        margin-bottom: 25px;
    }

    /* 题型徽章 */
    .q-type-badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 6px;
        font-size: 14px;
        font-weight: bold;
        color: white;
    }
    .badge-single { background-color: #10aeff; }
    .badge-multi { background-color: #b37feb; }

    /* 侧边栏统计数字放大 */
    .stat-box {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        margin-bottom: 15px;
        border: 1px solid rgba(255, 255, 255, 0.15);
    }
    .stat-num {
        font-size: 32px;
        font-weight: bold;
        color: #ffffff;
    }
    .stat-label {
        font-size: 13px;
        color: #cccccc;
    }

    /* 【核心】单选题选项卡片美化：改为大字号、带阴影、悬浮高亮的卡片 */
    div[data-testid="stHorizontalBlock"] div.stButton > button {
        background-color: #ffffff !important;
        color: #333333 !important;
        border: 1px solid #eaeaea !important;
        border-radius: 12px !important;
        padding: 20px 25px !important;
        font-size: 18px !important;
        font-weight: 500 !important;
        text-align: left !important;
        justify-content: flex-start !important;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05) !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
        margin-bottom: 12px !important;
        display: flex !important;
        align-items: center !important;
    }

    /* 选项卡片悬浮高亮效果 */
    div[data-testid="stHorizontalBlock"] div.stButton > button:hover {
        background-color: #e6f7ff !important;
        border-color: #1890ff !important;
        color: #1890ff !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1) !important;
    }

    /* 原生复选框样式字体放大（多选题保留 checkbox） */
    .stCheckbox p {
        font-size: 18px !important;
        font-weight: 500 !important;
    }

    /* 答题反馈卡片 */
    .result-card {
        padding: 20px;
        border-radius: 12px;
        margin: 20px 0;
        font-size: 18px;
    }
    .res-correct {
        background-color: #e6f7ff;
        border-left: 6px solid #1890ff;
        color: #0050b3;
    }
    .res-wrong {
        background-color: #fff1f0;
        border-left: 6px solid #ff4d4f;
        color: #a8071a;
    }
    </style>
    """, unsafe_allow_html=True)


# ==============================================================================
# 🛠️ 题库读取与核心解析引擎（动态解析本地 shauti.md）
# ==============================================================================
@st.cache_data(show_spinner="📚 正在动态载入并高精度清洗题库中...")
def load_and_parse_md(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return []

    lines = content.split('\n')
    questions = []
    current_q = None

    q_pattern = re.compile(r'^\s*(\d+)\.\s*(.*?\([ \t]*\*\*([A-Z\s]+)\*\*[ \t]*\).*)$')
    q_pattern_alt = re.compile(r'^\s*(\d+)\.\s*(.*?\([ \t]*([A-Z\s]+)[ \t]*\).*)$')

    for line in lines:
        line_str = line.strip()
        if not line_str:
            continue

        match = q_pattern.match(line_str) or q_pattern_alt.match(line_str)
        if match:
            if current_q:
                questions.append(current_q)
            ans = match.group(3).replace(' ', '').strip()
            current_q = {
                'text': line_str,
                'ans': ans,
                'options': []
            }
        else:
            if current_q and (line_str.startswith('A.') or line_str.startswith('B.') or
                              line_str.startswith('C.') or line_str.startswith('D.') or 'A.' in line_str):
                current_q['options'].append(line_str)

    if current_q:
        questions.append(current_q)

    def parse_options(opt_list):
        full_opts = []
        for opt in opt_list:
            parts = re.split(r'\s+([A-D]\.)', ' ' + opt.strip())
            parts = [p.strip() for p in parts if p.strip()]
            current_prefix = None
            for p in parts:
                if re.match(r'^[A-D]\.$', p):
                    current_prefix = p
                elif current_prefix:
                    full_opts.append(f"{current_prefix} {p}")
                    current_prefix = None
                else:
                    full_opts.append(p)
        opt_dict = {}
        for fo in full_opts:
            m = re.match(r'^([A-D])\.\s*(.*)$', fo)
            if m:
                opt_dict[m.group(1)] = m.group(2)
        return opt_dict

    cleaned_questions = []
    seen_features = set()

    for q in questions:
        pure_text = re.sub(r'^\s*\d+\.\s*', '', q['text'])
        pure_text = re.sub(r'\([ \t]*\*\*?[A-Z]+\*\*?[ \t]*\)', '()', pure_text).strip()

        feature = pure_text[:30]
        if feature in seen_features:
            continue
        seen_features.add(feature)

        opts = parse_options(q['options'])
        if not opts:
            opts = {"A": "暂无选项", "B": "暂无选项", "C": "暂无选项", "D": "暂无选项"}

        is_multi = len(q['ans']) > 1
        cleaned_questions.append({
            'type': 'multi' if is_multi else 'single',
            'title': pure_text,
            'options': opts,
            'answer': q['ans']
        })

    return cleaned_questions


# ============================================
# 🎮 主程序
# ============================================
inject_custom_css()

# 读取本地 md 题库文件
questions = load_and_parse_md('shauti.md')

if not questions:
    st.error("❌ 未能在当前文件夹找到 `shauti.md` 题库，请确保文件名与位置一致。")
    st.stop()

# 初始化Session State
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'show_analysis' not in st.session_state:
    st.session_state.show_analysis = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_mode' not in st.session_state:
    st.session_state.quiz_mode = "顺刷模式"
if 'shuffled_indices' not in st.session_state:
    st.session_state.shuffled_indices = list(range(len(questions)))

# ============================================
# 🧭 侧边栏：刷题控制与进度仪表盘
# ============================================
with st.sidebar:
    st.markdown("<h2 style='color:white; text-align:center;'>⚙️ 刷题工作台</h2>", unsafe_allow_html=True)
    st.markdown("---")

    # 仪表盘统计卡片
    st.markdown(f"""
    <div class="stat-box">
        <div class="stat-num">{len(questions)}</div>
        <div class="stat-label">题库总题量</div>
    </div>
    <div class="stat-box">
        <div class="stat-num">{st.session_state.score}</div>
        <div class="stat-label">已答对题数</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # 刷题模式选择
    with st.expander("🔄 切换刷题模式", expanded=True):
        mode = st.radio(
            "刷题模式",
            ["顺刷模式", "随机模式"],
            label_visibility="collapsed"
        )
        if mode != st.session_state.quiz_mode:
            st.session_state.quiz_mode = mode
            if mode == "随机模式":
                random.shuffle(st.session_state.shuffled_indices)
            else:
                st.session_state.shuffled_indices = list(range(len(questions)))
            st.session_state.current_index = 0
            st.session_state.show_analysis = False
            st.rerun()

    # 快捷跳题
    with st.expander("🔍 快捷跳转"):
        jump_idx = st.number_input(
            "题号",
            min_value=1,
            max_value=len(questions),
            value=st.session_state.current_index + 1
        )
        if st.button("🚀 跳转", use_container_width=True):
            st.session_state.current_index = jump_idx - 1
            st.session_state.show_analysis = False
            st.rerun()

    # 重置按钮
    if st.button("🚨 重置所有进度", use_container_width=True):
        st.session_state.current_index = 0
        st.session_state.score = 0
        st.session_state.show_analysis = False
        st.rerun()

# ============================================
# 📱 主内容区：全量大字号刷题大卡片
# ============================================
st.markdown("<div class='main-title'>📱 微信小程序开发题库</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>智能互动刷题系统 - 大字号护眼版</div>", unsafe_allow_html=True)

total_qs = len(questions)
current_real_idx = st.session_state.shuffled_indices[st.session_state.current_index]
q = questions[current_real_idx]

# 显示进度条
progress_val = (st.session_state.current_index + 1) / total_qs
st.progress(progress_val)
st.markdown(
    f"<p style='text-align: right; color: #777;'>当前进度：<b>{st.session_state.current_index + 1}</b> / {total_qs}</p>",
    unsafe_allow_html=True)

# 题型徽章和题目文本（大字号题目）
if q['type'] == 'single':
    st.markdown('<span class="q-type-badge badge-single">单选题</span>', unsafe_allow_html=True)
else:
    st.markdown('<span class="q-type-badge badge-multi">多选题</span>', unsafe_allow_html=True)

st.markdown(f'<div class="big-question-text">{st.session_state.current_index + 1}. {q["title"]}</div>',
            unsafe_allow_html=True)

# ------------------------------------------------------------------------------
# ⚡ 核心逻辑：【单选题】按钮化卡片改造
# ------------------------------------------------------------------------------
if q['type'] == 'single':
    st.write("请点击下方选项直接回答：")

    # 获取规范化的选项列表 ['A. xxx', 'B. xxx']
    options_raw = [f"{k}. {v}" for k, v in q['options'].items()]

    # 动态生成四个巨型按钮选项卡片（由于Streamlit列布局很难处理按钮悬浮高亮，采用直接渲染方式）
    col_opts = st.columns(1)  # 全部垂直拉满，更符合手机操作

    # 遍历选项，为每一个选项生成一个带悬浮效果的卡片按钮
    for raw_opt in options_raw:
        # 使用选项的核心内容 A. xxx 作为按钮 ID，防止 Streamlit 重复 Key 报错
        if col_opts[0].button(raw_opt, key=f"btn_{current_real_idx}_{raw_opt}", use_container_width=True):
            # 点击后直接进入评判逻辑
            user_choice = raw_opt[0]  # 获取 A, B, C, D

            if user_choice == q['answer']:
                if not st.session_state.show_analysis:
                    st.session_state.score += 1
                    # 答对了：不拖泥带水，瞬切到下一题
                    if st.session_state.current_index < total_qs - 1:
                        st.session_state.current_index += 1
                        st.rerun()
                    else:
                        st.balloons()
                        st.success("🎉 恭喜你，刷完了所有题目！")
            else:
                # 答错了：卡住不动，展示反馈和答案
                st.session_state.show_analysis = True
                # 记录用户点错的是哪个选项
                st.session_state.selected_wrong = raw_opt

    # 评判反馈区
    if st.session_state.show_analysis:
        st.markdown(f"""
        <div class="result-card res-wrong">
            <b>❌ 回答错误！</b><br>
            您的选择：{st.session_state.selected_wrong}<br>
            🎯 正确答案：<b>{q['answer']}</b>
        </div>
        """, unsafe_allow_html=True)

        # 提供一个下一题按钮继续
        if st.button("认识了考点，下一题 ➡️", use_container_width=True, type="primary"):
            st.session_state.show_analysis = False
            del st.session_state['selected_wrong']  # 清空临时状态
            if st.session_state.current_index < total_qs - 1:
                st.session_state.current_index += 1
                st.rerun()
            else:
                st.success("🎉 恭喜你，刷完了所有题目！")

# ------------------------------------------------------------------------------
# ⚡ 多选题逻辑：保留原 checkbox 样式（防止选项文本太长导致卡片撑破）
# ------------------------------------------------------------------------------
else:
    options_raw = [f"{k}. {v}" for k, v in q['options'].items()]
    selected_opts = []

    st.write("请勾选正确选项（多选）：")
    for opt in options_raw:
        # 多选框，保留 原 checkbox 样式，但字体放大
        checked = st.checkbox(opt, key=f"chk_{current_real_idx}_{opt[0]}")
        if checked:
            selected_opts.append(opt[0])

    # 并列双按钮：提交 和 下一题/跳过
    col_submit, col_next = st.columns([1, 1])

    with col_submit:
        submit = st.button("📥 提 交 答 案", use_container_width=True, type="secondary")
    with col_next:
        next_q = st.button("➡️ 下一题/跳过", use_container_width=True)

    if submit:
        user_multi_ans = "".join(sorted(selected_opts))
        correct = q['answer']
        st.session_state.show_analysis = True

        if user_multi_ans == correct:
            st.session_state.score += 1
            st.session_state.multi_feedback = ("correct", correct)
        else:
            st.session_state.multi_feedback = ("wrong", user_multi_ans if user_multi_ans else "未选择", correct)

    if next_q:
        st.session_state.show_analysis = False
        if 'multi_feedback' in st.session_state:
            del st.session_state['multi_feedback']
        if st.session_state.current_index < total_qs - 1:
            st.session_state.current_index += 1
            st.rerun()
        else:
            st.success("🎉 恭喜你，刷完了所有题目！")

    if st.session_state.show_analysis and 'multi_feedback' in st.session_state:
        status, *ans_data = st.session_state.multi_feedback
        if status == "correct":
            st.markdown(f"""
            <div class="result-card res-correct">
                ✅ 恭喜！多选题完全正确！标准答案：<b>{ans_data[0]}</b>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-card res-wrong">
                ❌ 多选结果不全或错选！您的选择：{ans_data[0]}<br>
                🎯 官方正确答案：<b>{ans_data[1]}</b>
            </div>
            """, unsafe_allow_html=True)