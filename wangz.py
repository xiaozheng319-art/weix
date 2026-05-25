import streamlit as st
import re
import random

# 设置网页基本配置
st.set_page_config(
    page_title="",
    page_icon="📱",
    layout="centered",
    initial_sidebar_state="expanded"
)


# ==============================================================================
# 🎨 现代高级纯净网站 CSS 样式（超级大字号、高端轻量渐变背景）
# ==============================================================================
def inject_custom_css():
    st.markdown("""
    <style>
    /* 干净高级的网页轻量微渐变背景 */
    .stApp {
        background: linear-gradient(135deg, #eef2f3 0%, #e4eefe 100%) !important;
    }

    /* 顶部主标题美化 */
    .main-title {
        font-size: 2.6rem !important;
        font-weight: 800 !important;
        color: #1a2a6c;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: 1px;
    }
    .sub-title {
        text-align: center;
        color: #5c6b73;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }

    /* 超大字号题目展示 */
    .big-question-text {
        font-size: 26px !important;
        font-weight: 700 !important;
        color: #0d1b2a;
        line-height: 1.6 !important;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    /* 题型专业标签 */
    .q-type-badge {
        display: inline-block;
        padding: 6px 14px;
        border-radius: 6px;
        font-size: 14px;
        font-weight: bold;
        color: white;
    }
    .badge-single { background-color: #0077b6; }
    .badge-multi { background-color: #7209b7; }

    /* 全局原生单选/复选框字号强力放大 */
    .stRadio p, .stCheckbox p {
        font-size: 20px !important;
        font-weight: 500 !important;
        color: #1f2937 !important;
        line-height: 1.5 !important;
    }

    .stRadio > div, .stCheckbox > div {
        padding: 6px 0;
    }

    /* 侧边栏专业统计卡片 */
    .stat-box {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 18px;
        text-align: center;
        margin-bottom: 15px;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }
    .stat-num {
        font-size: 34px;
        font-weight: 800;
        color: #ffffff;
    }
    .stat-label {
        font-size: 13px;
        color: #9cb1cc;
        margin-top: 4px;
    }

    /* 纯净答题反馈大卡片 */
    .result-card {
        padding: 22px;
        border-radius: 12px;
        margin: 25px 0;
        font-size: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    }
    .res-correct {
        background-color: #e8f5e9;
        border-left: 6px solid #2e7d32;
        color: #1b5e20;
    }
    .res-wrong {
        background-color: #ffebee;
        border-left: 6px solid #c62828;
        color: #b71c1c;
    }

    /* 操作按钮样式升级 */
    div.stButton > button {
        font-size: 18px !important;
        font-weight: 600 !important;
        padding: 12px 24px !important;
        border-radius: 10px !important;
        transition: all 0.2s ease;
    }
    </style>
    """, unsafe_allow_html=True)


# ==============================================================================
# 🛠️ 高精度题库文本动态解析器（动态解析本地 shauti.md）
# ==============================================================================
@st.cache_data(show_spinner="📚 正在实时解析本地 shauti.md 题库...")
def load_and_parse_md(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        return []

    lines = content.split('\n')
    questions = []
    current_q = None

    # 匹配形如：1. 下载文件使用的微信小程序接口是( **B** ) 或 ( **ABCD** )
    q_pattern = re.compile(r'^\s*(\d+)\.\s*(.*)\([ \t]*\*\*([A-Z]+)\*\*[ \t]*\)\s*$')

    for line in lines:
        line_str = line.strip()
        if not line_str:
            continue

        match = q_pattern.match(line_str)
        if match:
            if current_q:
                questions.append(current_q)
            ans = match.group(3).strip()
            title = match.group(2).strip() + " ( )"
            current_q = {
                'title': title,
                'ans': ans,
                'options_raw': []
            }
        else:
            if current_q and any(line_str.startswith(prefix) for prefix in ['A.', 'B.', 'C.', 'D.']):
                current_q['options_raw'].append(line_str)
            elif current_q and 'A.' in line_str and 'B.' in line_str:
                current_q['options_raw'].append(line_str)

    if current_q:
        questions.append(current_q)

    cleaned_questions = []
    for q in questions:
        opt_dict = {}
        full_opt_str = " ".join(q['options_raw'])

        matches = re.findall(r'([A-D])\.\s*(.*?)(?=\s+[A-D]\.|$)', full_opt_str)
        for m in matches:
            opt_dict[m[0]] = m[1].strip()

        if not opt_dict:
            opt_dict = {"A": "未正常读取到选项 A", "B": "未正常读取到选项 B", "C": "未正常读取到选项 C",
                        "D": "未正常读取到选项 D"}

        is_multi = len(q['ans']) > 1
        cleaned_questions.append({
            'type': 'multi' if is_multi else 'single',
            'title': q['title'],
            'options': opt_dict,
            'answer': q['ans']
        })

    return cleaned_questions


# ==============================================================================
# 🎮 初始化与状态机管控
# ==============================================================================
inject_custom_css()

# 直接读取本地的 'shauti.md'
questions = load_and_parse_md('微信小程序题库_全量单多选分类版.md')

if not questions:
    st.error("❌ 未能在当前文件夹找到 `shauti.md` 题库文件，请检查文件名与位置。")
    st.stop()

# 核心状态存储
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'show_analysis' not in st.session_state:
    st.session_state.show_analysis = False
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'quiz_mode' not in st.session_state:
    st.session_state.quiz_mode = "📖 顺序刷题"
if 'shuffled_indices' not in st.session_state:
    st.session_state.shuffled_indices = list(range(len(questions)))

# ==============================================================================
# 🧭 侧边栏：高级手风琴单列表样式（拉开关闭）
# ==============================================================================
with st.sidebar:
    st.markdown("<h2 style='color:white; text-align:center;'>🧭 刷题控制中心</h2>", unsafe_allow_html=True)
    st.markdown("---")

    # 仪表盘始终置顶可见，保持对正确率的掌控
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

    # 🗂️ 【单列表展开收起组 1】：刷题模式切换
    with st.expander("🔄 切换刷题模式", expanded=False):
        mode = st.radio(
            "选择当前的刷题模式：",
            ["📖 顺序刷题", "🎲 随机乱序"],
            label_visibility="collapsed"
        )
        if mode != st.session_state.quiz_mode:
            st.session_state.quiz_mode = mode
            if mode == "🎲 随机乱序":
                random.shuffle(st.session_state.shuffled_indices)
            else:
                st.session_state.shuffled_indices = list(range(len(questions)))
            st.session_state.current_index = 0
            st.session_state.show_analysis = False
            st.rerun()

    # 🗂️ 【单列表展开收起组 2】：精准跨越跳题
    with st.expander("🔍 快速跳转题号", expanded=False):
        jump_idx = st.number_input(
            "请输入目标题号：",
            min_value=1,
            max_value=len(questions),
            value=st.session_state.current_index + 1
        )
        if st.button("确定跳转", use_container_width=True):
            st.session_state.current_index = jump_idx - 1
            st.session_state.show_analysis = False
            st.rerun()

    # 🗂️ 【单列表展开收起组 3】：重置与进度清空
    with st.expander("🚨 重置答题进度", expanded=False):
        st.markdown(
            "<p style='color:#ff4d4f; font-size:13px;'>注意：此操作将清空您本次所有答题记录与得分，从第 1 题重新开始。</p>",
            unsafe_allow_html=True)
        if st.button("确认清空进度", use_container_width=True, type="primary"):
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.session_state.show_analysis = False
            st.rerun()

# ============================================
# 📱 主刷题大卡片区
# ============================================
st.markdown("<div class='main-title'>📱 微信小程序开发题库</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-title'>大字号护眼纯净版 · 完备控制流</div>", unsafe_allow_html=True)

total_qs = len(questions)
current_real_idx = st.session_state.shuffled_indices[st.session_state.current_index]
q = questions[current_real_idx]

# 横向顶端进度条
progress_val = (st.session_state.current_index + 1) / total_qs
st.progress(progress_val)
st.markdown(
    f"<p style='text-align: right; color: #555; font-weight: bold;'>当前进度：{st.session_state.current_index + 1} / {total_qs}</p>",
    unsafe_allow_html=True)

# 题型徽章与题目文本
if q['type'] == 'single':
    st.markdown('<span class="q-type-badge badge-single">单选题</span>', unsafe_allow_html=True)
else:
    st.markdown('<span class="q-type-badge badge-multi">多选题</span>', unsafe_allow_html=True)

st.markdown(f'<div class="big-question-text">{st.session_state.current_index + 1}. {q["title"]}</div>',
            unsafe_allow_html=True)

# 标准选项列表
options_mapping = [f"{k}. {v}" for k, v in q['options'].items()]

# ------------------------------------------------------------------------------
# ⚡ 单选题交互逻辑
# ------------------------------------------------------------------------------
if q['type'] == 'single':
    selected = st.radio(
        "请选择您的答案：",
        options_mapping,
        index=None,
        key=f"radio_idx_{st.session_state.current_index}",
        label_visibility="collapsed"
    )

    if selected:
        user_choice = selected[0]

        if user_choice == q['answer']:
            if not st.session_state.show_analysis:
                st.session_state.score += 1
                if st.session_state.current_index < total_qs - 1:
                    st.session_state.current_index += 1
                    st.rerun()
                else:
                    st.balloons()
                    st.success("🎉 太厉害了！您已经完成了全部题库的作答！")
        else:
            st.session_state.show_analysis = True

    if st.session_state.show_analysis:
        st.markdown(f"""
        <div class="result-card res-wrong">
            <b>❌ 回答错误！</b><br>
            您的选择是：<span style='font-weight:bold;'>{selected[0] if selected else '未选择'}</span><br>
            🎯 正确答案是：<span style='font-weight:bold; font-size:24px; color:#c62828;'>{q['answer']}</span>
        </div>
        """, unsafe_allow_html=True)

        if st.button("➡️ 进入下一题", type="primary", use_container_width=True):
            st.session_state.show_analysis = False
            if st.session_state.current_index < total_qs - 1:
                st.session_state.current_index += 1
                st.rerun()
            else:
                st.success("🎉 恭喜，您已刷完最后一道题！")

# ------------------------------------------------------------------------------
# ⚡ 多选题交互逻辑
# ------------------------------------------------------------------------------
else:
    chosen_multi = []
    st.write("请勾选所有正确选项：")
    for opt in options_mapping:
        is_checked = st.checkbox(opt, key=f"chk_{st.session_state.current_index}_{opt[0]}")
        if is_checked:
            chosen_multi.append(opt[0])

    user_multi_code = "".join(sorted(chosen_multi))

    # 并列双按钮
    btn_col1, btn_col2 = st.columns(2)
    with btn_col1:
        submit_multi = st.button("📥 提 交 答 案", use_container_width=True, type="secondary")
    with btn_col2:
        next_multi = st.button("➡️ 跳过 / 下一题", use_container_width=True)

    if submit_multi:
        if not user_multi_code:
            st.warning("⚠️ 请先至少勾选一个选项后再进行提交！")
        else:
            st.session_state.show_analysis = True
            if user_multi_code == q['answer']:
                st.session_state.is_multi_correct = True
                st.session_state.score += 1
            else:
                st.session_state.is_multi_correct = False

    if next_multi:
        st.session_state.show_analysis = False
        if 'is_multi_correct' in st.session_state:
            del st.session_state['is_multi_correct']
        if st.session_state.current_index < total_qs - 1:
            st.session_state.current_index += 1
            st.rerun()
        else:
            st.success("🎉 全量多选题部分已全部刷完！")

    if st.session_state.show_analysis:
        if st.session_state.get('is_multi_correct', False):
            st.markdown(f"""
            <div class="result-card res-correct">
                <b>✅ 回答完全正确！</b><br>
                正确答案组合：<span style='font-weight:bold; font-size:24px;'>{q['answer']}</span>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-card res-wrong">
                <b>❌ 回答错误或选项不全！</b><br>
                您的选择：<span style='font-weight:bold;'>{user_multi_code}</span><br>
                🎯 正确答案组合：<span style='font-weight:bold; font-size:24px; color:#c62828;'>{q['answer']}</span>
            </div>
            """, unsafe_allow_html=True)