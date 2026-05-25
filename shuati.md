# 微信小程序开发题库（全量分类去重版）

> 已经为您将原始文件中的 **510道题目** 进行了全局深度去重和校对，最终清洗出 **单选题 299道**，**多选题 150道**。所有单选和多选已各自合并归类，并重新按顺序进行了编号。
 
## 一、单选题汇总（共 299 题）

1. 下载文件使用的微信小程序接口是( **B** )
   A. wx.saveFile  B. wx.downloadFile  C. wx.loadFile  D. wx.fetchFile

2. 在微信小程序中，用于异步写入本地缓存的接口是( **D** )
   A. wx.getStorage  B. wx.clearStorage  C. wx.removeStorage  D. wx.setStorage

3. 打开微信客服功能时，课程中提到其适用前提是( **C** )
   A. 只要有头像权限即可  B. 个人小程序即可  C. 必须是企业小程序  D. 必须开通云开发

4. 在 button 上设置用于选择微信头像的 open-type 是( **A** )
   A. chooseAvatar  B. getUserInfo  C. openAvatar  D. getAvatar

5. 课程中提到，读取本地缓存时必须传入的参数是( **D** )
   A. url  B. type  C. data  D. key

6. 若要打开微信内置地图查看某个经纬度位置，应使用( **C** )
   A. wx.mapLocation  B. wx.openMap  C. wx.openLocation  D. wx.showMap

7. 上传文件到服务器使用的接口是( **D** )
   A. wx.chooseImage  B. wx.downloadFile  C. wx.request  D. wx.uploadFile

8. 如果要一次性清除小程序中的所有缓存数据，应使用( **B** )
   A. wx.deleteAllStorage  B. wx.clearStorage  C. wx.removeStorage  D. wx.resetStorage

9. 在较新的基础库版本中，获取用户昵称更推荐的方式是( **A** )
   A. 通过 input 输入昵称  B. 使用 wx.getUserProfile  C. 通过 map 组件填写昵称  D. 使用 wx.getUserInfo

10. 在 wx.openDocument 中，如果希望显示右上角菜单按钮，需要设置的参数是( **C** )
   A. showButton  B. showTopMenu  C. showMenu  D. showRightMenu

11. 下列哪一个接口表示同步读取本地缓存?( **C** )
   A. wx.clearStorageSync  B. wx.setStorageSync  C. wx.getStorageSync  D. wx.removeStorageSync

12. 微信小程序登录时，用于获取登录凭证 code 的接口是( **D** )
   A. wx.authorize  B. wx.request  C. wx.getUserInfo  D. wx.login

13. 课程中提到，在多数普通开发场景下，推荐调用的地理位置接口是( **A** )
   A. wx.getLocation  B. wx.getFuzzyLocation  C. wx.chooseAddress  D. wx.openLocation

14. 在小程序中，选择用户位置所使用的接口是( **A** )
   A. wx.chooseLocation  B. wx.openLocation  C. wx.selectLocation  D. wx.getLocation

15. 课程中提到，小程序前端获取 code 后，下一步通常是( **A** )
   A. 调用后台接口换取登录态  B. 直接拉起支付  C. 直接写入本地缓存  D. 直接获取 openid

16. 在小程序缓存接口中，带有 Sync 后缀的方法表示( **D** )
   A. 加密接口  B. 回调接口  C. 网络接口  D. 同步接口

17. 在小程序中拉起微信支付使用的接口是( **A** )
   A. wx.requestPayment  B. wx.pay  C. wx.requestPay  D. wx.openPayment

18. 删除指定 key 对应缓存数据的接口是( **A** )
   A. wx.removeStorage  B. wx.cleanStorage  C. wx.deleteStorage  D. wx.clearStorage

19. 用于打开文档文件的微信小程序接口是( **D** )
   A. wx.readDocument  B. wx.showDocument  C. wx.loadDocument  D. wx.openDocument

20. 在获取用户地理位置之前，首先要做的是( **A** )
   A. 获取用户授权  B. 创建地图组件  C. 配置 request 域名  D. 调用支付接口
   ## 二. 多选题（共10题，34分）

21. 在微信小程序的目录结构中，用于管理小程序全局配置(如导航栏颜色、页面路径等)的文件是？( **B** )
   A. app.js
   B. app.json
   C. app.wxss
   D. project.config.json

22. 微信小程序中，相当于传统Web前端开发中HTML文件，用于搭建页面结构的标签文件是？( **D** )
   A. .wxss
   B. .js
   C. .json
   D. .wxml

23. 微信小程序全新的渲染引擎 Skyline 相比于传统的 WebView 引擎，在架构上做出了什么重大改变以提升性能？( **B** )
   A. 强制将渲染和业务逻辑合并在同一条线程上执行
   B. 采用双线程架构，使渲染线程与逻辑线程相互独立，避免逻辑阻塞界面
   C. 完全废弃了 WXML 和 WXSS 代码规范
   D. 将所有的计算都转移给第三方服务器进行处理

24. 在微信小程序的通信模型中，主要负责处理页面布局和样式显示的是哪一层？( **B** )
   A. 逻辑层
   B. 渲染层
   C. 物理层
   D. 数据层

25. 当用户在使用小程序时，按下手机的 Home 键将小程序切换到后台运行，此时会触发小程序的哪一个应用级别的生命周期函数？( **D** )
   A. onLaunch
   B. onShow
   C. onReady
   D. onHide

26. 在页面级别的生命周期函数中，通常建议将“页面初始化数据”(如发起网络请求获取默认数据)的操作放在哪一个函数中执行？( **A** )
   A. onLoad
   B. onShow
   C. onReady
   D. onUnload

27. 在小程序的 WXML 文件中，如果想要把定义在 JS 文件 data 中的变量 sum 动态绑定并渲染到页面上，正确的语法格式是？( **B** )
   A. {sum}
   B. {{sum}}
   C. ${sum}
   D. <sum>

28. 在小程序代码逻辑中，若想动态更新页面数据并实现视图层的同步渲染，必须通过以下哪种方式修改数据？( **C** )
   A. 直接使用 this.data.变量名 = 新值
   B. 使用 this.updateData({ 变量名: 新值 })
   C. 使用 this.setData({ 变量名: 新值 })
   D. 修改 DOM 节点的 innerText

29. 如果页面中有一个元素需要非常频繁地切换显示与隐藏状态，从性能优化的角度考虑，推荐使用哪一种条件渲染方式？( **D** )
   A. wx:if
   B. block 包裹
   C. display: inline
   D. hidden 属性

30. 使用 wx:for 进行列表渲染时，如果不使用 wx:for-item 去特别指定，默认代表循环中“当前遍历项”的变量名是？( **B** )
   A. index
   B. item
   C. key
   D. element

31. 在给小程序组件绑定点击事件时，如果想要阻止该事件向父节点继续传递(即阻止事件冒泡)，应该使用以下哪种绑定语法？( **B** )
   A. bindtap
   B. catchtap
   C. ontap
   D. preventtap

32. 在事件处理函数的 event 对象中，用来表示“当前绑定了事件处理函数的组件”的属性是哪一个？( **D** )
   A. target
   B. type
   C. timeStamp
   D. currentTarget

33. 如果想在全局配置文件中指定小程序导航栏的标题文字、背景色等样式，应该在 app.json 的哪个属性中进行设置？( **B** )
   A. pages
   B. window
   C. tabBar
   D. style

34. 当一个单独页面的 page.json 配置项与全局的 app.json 配置项发生冲突时(例如都设置了导航栏背景色)，最终会如何显示？( **C** )
   A. 报错无法渲染页面
   B. 优先以 app.json 的配置为准
   C. 优先以 page.json 的配置为准，覆盖全局配置
   D. 随机显示其中一种配置

35. 在微信小程序的基础组件中，如果想要实现图片的等比缩放，且保证图片的短边能完全显示出来(长边可能被裁剪)，应将 image 组件的 mode 属性设置为什么？( **C** )
   A. scaleToFill
   B. aspectFit
   C. aspectFill
   D. widthFix

36. 在Flex布局中，想要实现主轴上的项目均匀分布，且每个项目两侧的间隔相等，应该将 justify-content 属性设置为什么？( **C** )
   A. center
   B. space-between
   C. space-around
   D. flex-start

37. 微信小程序提供了一个独有的解决屏幕自适应的像素单位，不论什么机型，官方规定屏幕的默认宽度总是多少？( **C** )
   A. 320
   B. 375
   C. 750
   D. 1080

38. 在实际开发中，微信官方建议设计师在出视觉设计稿时，以哪一款手机的屏幕尺寸作为标准度量进行设计？( **B** )
   A. iPhone 5
   B. iPhone 6
   C. iPhone X
   D. iPhone 12

39. 使用 navigator 组件进行页面跳转时，哪种 open-type 会导致“当前页面出栈，新页面入栈”，且左上角没有返回按钮？( **B** )
   A. navigate
   B. redirect
   C. switchTab
   D. reLaunch

40. 小程序的页面栈管理遵循的是什么数据结构原则？( **C** )
   A. 先进先出
   B. 随机出入
   C. 后进先出
   D. 树状结构

41. 在配置小程序的 tabBar 时，list 属性数组中的选项数量有什么严格的限制要求？( **C** )
   A. 最少1个，最多3个
   B. 最少2个，最多4个
   C. 最少2个，最多5个
   D. 没有数量限制

42. 当把 tabBar 的 position 属性设置为 top(顶部)时，tabBar 的显示效果会发生什么变化？( **A** )
   A. 只显示图标，不显示文字
   B. 只显示文字，不显示图标
   C. 图标和文字都正常显示
   D. tabBar会直接隐藏

43. 在普通页面的js文件中，如果想要获取定义在 app.js 里的 globalData 全局数据，首先需要调用哪个官方提供的方法？( **D** )
   A. require()
   B. wx.getGlobal()
   C. this.data()
   D. getApp()

44. 如果想在全局样式文件 app.wxss 或某个页面的 wxss 中引入一个第三方的通用外部样式文件，应该使用以下哪种语法？( **A** )
   A. @import
   B. <import src="...">
   C. require(...)
   D. import "..."

45. 1. 获取全局应用实例对象的正确方法是( **B** )
   A. new App()
   B. getApp()
   C. this.getApp()
   D. wx.getApplication()

46. 在课程中，获取页面栈所使用的方法是( **C** )
   A. getPageStack()
   B. wx.getPages()
   C. getCurrentPages()
   D. getPages()

47. 在小程序中，哪一个 API 用于动态设置当前页面的导航栏标题？( **C** )
   A. wx.setTitle
   B. wx.setPageTitle
   C. wx.setNavigationBarTitle
   D. wx.navigationTitle

48. 在事件处理函数中，获取当前绑定组件自定义属性值通常使用( **B** )
   A. e.dataset.currentTarget
   B. e.currentTarget.dataset
   C. e.detail.dataset
   D. e.target.value

49. 微信小程序中用于发起网络请求的核心 API 是( **D** )
   A. wx.http
   B. wx.fetch
   C. wx.ajax
   D. wx.request

50. 以下哪一个 API 可以在页面中显示带标题文本的 loading 提示框？( **B** )
   A. wx.showNavigationBarLoading
   B. wx.showLoading
   C. wx.showModal
   D. wx.showToast

51. 相较于 GET 请求，POST 请求的一个显著特点是( **B** )
   A. 安全性一定为零
   B. 更适合提交大量数据
   C. 无法携带参数
   D. 参数只能写在 URL 中

52. 课程中提到的页面分享给好友所对应的事件处理函数是( **C** )
   A. onAddToFavorites
   B. onShareTimeline
   C. onShareAppMessage
   D. onPageShare

53. 在目标页面接收 navigateTo 传递参数时，通常在哪个生命周期中通过 options 获取？( **A** )
   A. onLoad
   B. onHide
   C. onReady
   D. onShow

54. 关于小程序 request 合法域名配置，下列哪项说法是正确的？( **C** )
   A. 可以直接使用 IP 地址
   B. 必须配置父域名，不能配子域名
   C. 域名必须经过 ICP 备案
   D. 可以直接使用 localhost

55. 当组件上设置了 data-id="1001" 时，在事件函数中获取该值的正确方式是( **B** )
   A. e.target.id
   B. e.currentTarget.dataset.id
   C. e.dataset.id
   D. e.currentTarget.data.id

56. 课程中提到，小程序 request 合法域名配置时，域名必须使用( **C** )
   A. http
   B. ws
   C. https
   D. ftp

57. 课程中提到，设置导航栏颜色时，白色到红色渐变中的“白色”对应的是( **D** )
   A. 页面背景色
   B. 阴影色
   C. 边框色
   D. 前景色

58. 课程中提到的第二种页面传参方式是通过( **D** )
   A. 页面 JSON 配置
   B. 云开发数据库
   C. 本地缓存
   D. 全局数据 globalData

59. 在小程序页面跳转并携带参数时，课程中介绍的主要 API 是( **B** )
   A. wx.pageTo
   B. wx.navigateTo
   C. wx.redirectUrl
   D. wx.openPage

60. 在微信小程序中，用于给组件传递自定义参数的属性写法是( **B** )
   A. prop-*
   B. data-*
   C. attr-*
   D. custom-*

61. 在 wx.request 中，哪个参数是必填的，用于指定服务器接口地址？( **A** )
   A. url
   B. header
   C. method
   D. data

62. 开启页面下拉刷新的局部配置项是( **D** )
   A. pagePullDown
   B. onReachBottomDistance
   C. pullRefreshEnable
   D. enablePullDownRefresh

63. 如果要在小程序中获取数据，课程建议优先使用哪种请求方式？( **A** )
   A. GET
   B. DELETE
   C. TRACE
   D. PUT

64. 课程中第三种页面传参方式，是通过什么机制给上一个页面设置数据？( **D** )
   A. 本地存储
   B. 事件总线
   C. 云函数
   D. 页面栈

65. 1. 下载文件使用的微信小程序接口是( **B** )
   A. wx.saveFile
   B. wx.downloadFile
   C. wx.loadFile
   D. wx.fetchFile

66. 下列哪一个接口表示同步读取本地缓存？( **C** )
   A. wx.clearStorageSync
   B. wx.setStorageSync
   C. wx.getStorageSync
   D. wx.removeStorageSync

67. 1. 在页面中局部引入自定义组件时，需要使用的配置字段是( **C** )
   A. componentList
   B. componentMap
   C. usingComponents
   D. importComponents

68. 自定义组件创建完成后，默认会生成几个文件？( **C** )
   A. 5个
   B. 2个
   C. 4个
   D. 3个

69. 课程中提到，组件实例进入页面节点树时常用的生命周期是( **D** )
   A. ready
   B. moved
   C. created
   D. attached

70. 在组件的 json 文件中，表明当前文件是组件而不是页面的关键配置项是( **A** )
   A. "component": true
   B. "isComponent": true
   C. "type": "component"
   D. "page": true

71. 在组件中，事件处理函数通常定义在( **C** )
   A. options
   B. observers
   C. methods
   D. pageLifetimes

72. 如果需要监听组件数据变化，应使用的配置项是( **B** )
   A. watchers
   B. observers
   C. reacts
   D. listeners

73. 组件化开发的核心思想是将大型项目拆分为( **C** )
   A. 多个数据库表
   B. 多个测试账号
   C. 多个独立且可复用的小组件
   D. 多个服务器节点

74. 对于对象内部某个属性的变化监听，课程中强调应采用( **D** )
   A. 只监听对象名即可
   B. 只能在页面中监听
   C. 只能通过 methods 手动判断
   D. 深度监听对象内部字段

75. 在组件中，接收外部传入数据应定义在( **A** )
   A. properties
   B. methods
   C. observers
   D. data

76. 创建自定义组件时，应在开发工具中选择新建( **C** )
   A. Plugin
   B. App
   C. Component
   D. Page

77. 下列哪一项最符合课程中对“组件”的描述？( **A** )
   A. 具有特定功能且可重复使用的代码单元
   B. 只能表示页面中的文本
   C. 只能用于样式布局
   D. 只能由官方提供，不能自定义

78. 组件自身生命周期函数应定义在( **D** )
   A. methods
   B. options
   C. pageLifetimes
   D. lifetimes

79. 在组件中，内部自己维护的数据应定义在( **C** )
   A. behaviors
   B. lifetimes
   C. data
   D. properties

80. 在微信小程序中，自定义组件通常建议统一放在什么文件夹中管理？( **A** )
   A. components
   B. services
   C. utils
   D. pages

81. 用于组件之间共享代码、数据和方法的对象是( **C** )
   A. slots
   B. storage
   C. behaviors
   D. globalData

82. 在组件中用于占位、接收外部传入标签内容的机制是( **A** )
   A. slot
   B. template
   C. props
   D. mixin

83. 下列哪一项属于组件化开发的优势？( **A** )
   A. 方便团队并行开发
   B. 使页面结构更加混乱
   C. 降低代码复用率
   D. 增加代码冗余

84. 当组件中存在多个插槽时，正确的做法是( **C** )
   A. 只给第一个插槽命名
   B. 所有插槽都不命名
   C. 给每个插槽分别命名
   D. 用 id 区分即可

85. 如果一个自定义组件会在多个页面中频繁使用，更适合采用哪种引入方式？( **A** )
   A. 全局引入
   B. 局部引入
   C. 条件引入
   D. 动态引入

86. 在组件的 .js 文件中，用于注册组件的方法是( **B** )
   A. Page()
   B. Component()
   C. App()
   D. Create()

87. 1. 在小程序中，默认启动页面和 tabBar 页面必须放在( **B** )
   A. 任意包中
   B. 主包中
   C. 分包中
   D. 独立分包中

88. 下列关于用时注入的描述，正确的是( **A** )
   A. 只有真正渲染到该组件时才会注入
   B. 页面加载时全部组件都会立即注入
   C. 只能用于主包组件
   D. 必须关闭按需注入才能使用

89. 下列哪一种启动方式是指小程序被完全销毁后再次打开，需要重新加载？( **C** )
   A. 预启动
   B. 热启动
   C. 冷启动
   D. 二次启动

90. 在 app.json 中开启按需注入时，课程中提到的配置属性是( **B** )
   A. usingComponents
   B. lazyCodeLoading
   C. subpackages
   D. preloadRule

91. 在性能优化中，频繁调用 setData 可能带来的问题是( **A** )
   A. 页面渲染压力增大
   B. 页面更流畅
   C. 图片更清晰
   D. 分包体积更小

92. 骨架屏的主要作用是( **C** )
   A. 自动压缩图片资源
   B. 替代分包机制
   C. 在页面加载前展示内容轮廓，缓解等待感
   D. 替代真实数据长期展示

93. 小程序性能优化的主要目标之一是( **A** )
   A. 提升用户体验
   B. 增加代码体积
   C. 增加后台接口数量
   D. 减少页面数量

94. 小程序从用户打开到首页渲染完毕为止，这个过程称为( **A** )
   A. 小程序启动
   B. 页面加载
   C. 页面刷新
   D. 代码注入

95. 分包的主要作用之一是( **D** )
   A. 替代主包存在
   B. 让所有资源共享
   C. 强制所有页面一起加载
   D. 优化首次启动加载时间

96. 独立分包与普通分包相比，最大的特点是( **D** )
   A. 体积一定更小
   B. 必须包含 tabBar 页面
   C. 可以引用所有包的私有资源
   D. 可以脱离主包独立运行

97. 1. 下列哪一项不属于课程中提到的云开发优势？( **D** )
   A. 无需搭建服务器
   B. 一个后端环境可支持多端应用
   C. 可免登录免鉴权调用部分开放能力
   D. 必须提前购买固定资源包

98. 云开发文件上传后得到的、后续展示和处理都很重要的标识是( **A** )
   A. fileID
   B. appId
   C. openid
   D. envId

99. 下列哪一个能力是指“在云端运行的代码”？( **C** )
   A. 云存储
   B. 云托管
   C. 云函数
   D. 云数据库

100. 在云数据库数组条件查询中，若要查询“包含 1、3、4”的记录，应使用( **D** )
   A. db.command.and
   B. db.command.eq
   C. db.command.nin
   D. db.command.in

101. 云存储的一个典型特点是( **A** )
   A. 自带 CDN 加速，支持前端直接上传下载
   B. 只能存储结构化数据
   C. 只能在服务器端下载
   D. 只能存储文本文件

102. 在 project.config.json 中，用于指定本地云函数根目录的字段是( **C** )
   A. functionRoot
   B. cloudPath
   C. cloudfunctionRoot
   D. cloudRoot

103. 在云数据库中，查询集合全部数据通常使用的方法是( **D** )
   A. add()
   B. update()
   C. remove()
   D. get()

104. 云开发最突出的特点之一是开发者( **C** )
   A. 必须自行搭建服务器
   B. 必须单独购买数据库
   C. 无需搭建服务器即可开发业务
   D. 只能开发小程序前端页面

105. 在云开发中创建地理位置点时，课程中使用的方法是( **B** )
   A. db.map.point()
   B. db.geo.point()
   C. db.gps.point()
   D. db.location.point()

106. 云开发控制台中，用于管理集合记录、权限和索引的模块是( **D** )
   A. 概览
   B. 运营分析
   C. 云函数
   D. 数据库

107. 微信云开发是由谁联合推出的专业小程序开发服务？( **A** )
   A. 微信团队与腾讯云
   B. 微信团队与阿里云
   C. 微信团队与华为云
   D. 微信团队与百度智能云

108. 课程中提到，云数据库属于( **B** )
   A. 图数据库
   B. 文档型数据库
   C. 时序数据库
   D. 关系型数据库

109. 在小程序端调用云函数时，使用的核心 API 是( **A** )
   A. wx.cloud.callFunction
   B. wx.cloud.invoke
   C. wx.cloud.useFunction
   D. wx.cloud.runFunction

110. 在小程序端初始化云开发能力时，通常需要调用的方法是( **B** )
   A. wx.cloud.start()
   B. wx.cloud.init()
   C. wx.cloud.use()
   D. wx.cloud.open()

111. 在微信开发者工具中创建带云开发能力的小程序时，项目初始化需要选择( **C** )
   A. 小游戏模板
   B. 插件模板
   C. 微信云开发
   D. 公众号模板

112. 课程中提到，云开发模式相比传统开发模式，主要体现为( **C** )
   A. 无法支持前后端协作
   B. 环节更多、更复杂
   C. 更快捷方便
   D. 完全不需要产品经理

113. 如果想把 fileID 转换成浏览器可访问的临时网络链接，应调用( **D** )
   A. wx.cloud.downloadFile
   B. wx.cloud.getFilePath
   C. wx.cloud.openFile
   D. wx.cloud.getTempFileURL

114. 课程中“云代办”小程序的数据设计里，用于表示任务状态的字段是( **C** )
   A. desc
   B. tag
   C. status
   D. title

115. 在云函数模板中，event 参数主要表示( **C** )
   A. 数据库对象
   B. 定时器表达式
   C. 小程序端传入的参数及自动注入信息
   D. 存储配置

116. 如果希望只返回某些指定字段，而不是整条记录所有字段，应使用( **D** )
   A. doc()
   B. orderBy()
   C. where()
   D. field()

117. 云调用的本质是( **B** )
   A. 浏览器直接调用数据库
   B. 基于云函数使用小程序开放接口
   C. 本地缓存调用远程 API
   D. 前端直接访问支付接口

118. 在云开发中创建地理位置点时，使用的方法是( **D** )
   A. db.location.point()
   B. db.gps.point()
   C. db.map.point()
   D. db.geo.point()

119. 在发送邮件示例中，课程以哪种邮箱为例讲解授权码获取？( **D** )
   A. 企业微信邮箱
   B. Outlook
   C. Gmail
   D. QQ邮箱

120. 课程中提到，云函数运行环境基于( **C** )
   A. Java
   B. Go
   C. Node.js
   D. Python

121. 课程中生成小程序码使用的云调用接口是( **B** )
   A. wxacode.get
   B. wxacode.getUnlimited
   C. qrcode.create
   D. code.generate

122. 在课程加法示例中，云函数 add 最终返回的是( **C** )
   A. a 与 b 的乘积
   B. a 与 b 的差
   C. a 与 b 的和
   D. a 与 b 的平均值

123. 在云函数模板中，表示小程序端传入参数及部分自动注入信息的是( **D** )
   A. options
   B. result
   C. context
   D. event

124. 上传文件到云存储成功后，最重要的返回标识之一是( **B** )
   A. envId
   B. fileID
   C. orderId
   D. appId

125. 在小程序端调用云函数的核心 API 是( **D** )
   A. wx.cloud.execFunction
   B. wx.cloud.runFunction
   C. wx.cloud.useFunction
   D. wx.cloud.callFunction

126. 在课程正则查询示例中，主要匹配的是( **D** )
   A. location 字段
   B. count 字段中的数字
   C. image 字段
   D. name 字段中符合规律的字符串

127. 在云调用前，课程中提到要先确认接口是否( **A** )
   A. 支持云调用
   B. 支持本地缓存
   C. 支持多语言
   D. 支持 HTTPS

128. 云代办小程序中，用于表示任务标题的字段是( **B** )
   A. taskName
   B. title
   C. label
   D. name

129. 云开发数据库预设的常用权限数量是( **C** )
   A. 3种
   B. 2种
   C. 4种
   D. 5种

130. “所有用户可读，仅创建者可写” 更适合哪类数据？( **A** )
   A. 商品评论等公开数据
   B. 用户私密订单
   C. 系统配置密钥
   D. 后台流水信息

131. 在云函数中获取用户 openID、appID 等可信信息时，课程中使用的方法是( **B** )
   A. wx.getUserInfo()
   B. cloud.getWXContext()
   C. wx.login()
   D. cloud.getToken()

132. 在云函数中安装第三方 npm 包，课程中举的工具库示例是( **B** )
   A. vue
   B. lodash
   C. axios
   D. echarts

133. 图片内容安全检测成功时，返回的 errorCode 通常为( **C** )
   A. 1
   B. 200
   C. 0
   D. -1

134. 发送订阅消息时，在云函数配置文件中应声明的权限名称是( **C** )
   A. subscribeMessage
   B. subscribe.send
   C. subscribeMessage.send
   D. template.send

135. 云代办小程序中，用于保存任务经纬度信息的字段是( **B** )
   A. coordinate
   B. locationGPS
   C. gps
   D. point

136. 如果要把 fileID 转为浏览器可访问的临时链接，应调用( **C** )
   A. wx.cloud.downloadFile
   B. wx.cloud.getFilePath
   C. wx.cloud.getTempFileURL
   D. wx.cloud.openFile

137. 云开发模式下，课程中强调主要由哪类人员完成开发工作？( **A** )
   A. 前端人员
   B. 后端人员
   C. 测试人员
   D. 运维人员

138. 下列哪一项不属于课程中提到的云开发优势？( **A** )
   A. 必须自建后台管理系统
   B. 多端复用业务代码与数据
   C. 免登录免鉴权调用部分能力
   D. 按量计费

139. 云开发控制台中，可查看小程序访问记录和资源使用情况的模块是( **C** )
   A. 存储
   B. 权限管理
   C. 运营分析
   D. 数据库

140. 使用云开发能力前，需要先做的操作是( **B** )
   A. 先绑定客服
   B. 先开通云开发环境
   C. 先接入支付
   D. 先发布小程序

141. 在创建一个包含云开发能力的小程序时，初始化阶段应选择( **B** )
   A. 企业微信模板
   B. 微信云开发
   C. 插件模板
   D. 小游戏模板

142. 下列哪项能力是指“在云端运行的代码”？( **C** )
   A. 云数据库
   B. 云存储
   C. 云函数
   D. 云托管

143. 云开发控制台中，用于查看资源总体使用情况的模块是( **C** )
   A. 云函数
   B. 数据库
   C. 概览
   D. 存储

144. 在云数据库中，查询集合全部数据通常使用的方法是( **A** )
   A. get()
   B. update()
   C. add()
   D. remove()

145. 课程中提到，云开发模式相比传统开发模式，主要体现为( **A** )
   A. 更快捷方便
   B. 完全不需要产品经理
   C. 环节更多、更复杂
   D. 无法支持前后端协作

146. 云开发支持“一个后端环境服务多个端”，这体现的是( **A** )
   A. 多端复用
   B. 自动扩容
   C. 本地缓存
   D. 离线运行

147. 云存储的典型特点是( **C** )
   A. 只能存文本
   B. 只能存结构化数据
   C. 支持前端直接上传下载
   D. 只能后端下载

148. 课程中提到，云开发的计费方式主要是( **C** )
   A. 固定年费
   B. 免费无限用
   C. 按量计费
   D. 一次性买断

149. 若要查询“不包含 1、3、4”的记录，应使用( **D** )
   A. db.command.in
   B. db.command.eq
   C. db.command.neq
   D. db.command.nin

150. 在小程序端初始化云开发能力时，通常调用的方法是( **B** )
   A. wx.cloud.begin()
   B. wx.cloud.init()
   C. wx.cloud.use()
   D. wx.cloud.start()

151. 在云数据库数组条件查询中，查询“包含 1、3、4”的记录应使用( **A** )
   A. db.command.in
   B. db.command.eq
   C. db.command.and
   D. db.command.or

152. 若希望数据库查询结果只返回指定字段，应使用( **B** )
   A. where()
   B. field()
   C. doc()
   D. orderBy()

153. 在云开发中创建地理位置点时，课程中使用的方法是( **A** )
   A. db.geo.point()
   B. db.gps.point()
   C. db.map.point()
   D. db.location.point()

154. 在 project.config.json 中，用于指定云函数本地根目录的字段是( **C** )
   A. cloudDir
   B. cloudRoot
   C. cloudfunctionRoot
   D. functionRoot

155. 在传统小程序开发模式中，通常需要哪三类角色协作？( **C** )
   A. 后端、测试、采购
   B. 前端、运营、客服
   C. 前端、后端、运维
   D. 前端、设计、财务

156. 若要把 fileID 转换为浏览器可访问的临时链接，应调用( **A** )
   A. wx.cloud.getTempFileURL
   B. wx.cloud.downloadFile
   C. wx.cloud.previewFile
   D. wx.cloud.getFileInfo

157. 下列哪一项不属于课程中提到的云开发优势？( **D** )
   A. 按量计费
   B. 免登录免鉴权调用部分开放能力
   C. 多端复用业务代码与数据
   D. 必须自建后台管理系统

158. 传统小程序开发模式通常涉及的主要角色不包括( **B** )
   A. 运维
   B. 配音师
   C. 后端
   D. 前端

159. 云调用的本质是( **D** )
   A. 页面直接调用支付接口
   B. 本地缓存调用远程接口
   C. 浏览器直接调用数据库
   D. 基于云函数使用微信开放接口

160. 云代办小程序中，用于保存任务经纬度信息的字段是( **A** )
   A. locationGPS
   B. gps
   C. coordinate
   D. point

161. 云调用的本质是( **C** )
   A. 本地缓存调用远程 API
   B. 前端直接访问支付接口
   C. 基于云函数使用小程序开放接口
   D. 浏览器直接调用数据库

162. 云代办小程序中，用于表示任务状态的字段是( **B** )
   A. sort
   B. status
   C. desc
   D. name

163. 上传文件到云存储成功后，后续展示和处理都要用到的重要标识是( **A** )
   A. fileID
   B. envId
   C. appid
   D. openid

164. 云开发模式下，课程中强调的主要开发角色是( **B** )
   A. 后端人员
   B. 前端人员
   C. 测试人员
   D. 运维人员

165. 在小程序端初始化云开发能力时，通常调用的方法是( **C** )
   A. wx.cloud.begin()
   B. wx.cloud.use()
   C. wx.cloud.init()
   D. wx.cloud.start()

166. 课程中生成小程序码使用的云调用接口是( **A** )
   A. wxacode.getUnlimited
   B. qrcode.create
   C. wxacode.get
   D. code.generate

167. 若要查询“不包含 1、3、4”的记录，应使用( **B** )
   A. db.command.neq
   B. db.command.nin
   C. db.command.eq
   D. db.command.in

168. 云代办小程序中，用于表示任务状态的字段是( **D** )
   A. name
   B. desc
   C. sort
   D. status

169. 在小程序端调用云函数的核心 API 是( **B** )
   A. wx.cloud.execFunction
   B. wx.cloud.callFunction
   C. wx.cloud.useFunction
   D. wx.cloud.runFunction

170. 云开发控制台中，用于查看资源总体使用情况的模块是( **B** )
   A. 数据库
   B. 概览
   C. 存储
   D. 云函数

171. 下列哪一项不属于课程中提到的云开发优势？( **C** )
   A. 多端复用业务代码与数据
   B. 免登录免鉴权调用部分开放能力
   C. 必须自建后台管理系统
   D. 按量计费

172. 传统小程序开发模式通常涉及的主要角色不包括( **A** )
   A. 配音师
   B. 后端
   C. 运维
   D. 前端

173. 云存储的典型特点是( **D** )
   A. 只能后端下载
   B. 只能存文本
   C. 只能存结构化数据
   D. 支持前端直接上传下载

174. 上传文件到云存储成功后，最重要的返回标识之一是( **A** )
   A. fileID
   B. appId
   C. orderId
   D. envId

175. 1. 在课程案例中，电商小程序主要使用哪种技术模式进行开发？( **A** )
   A. 云开发
   B. 原生 Android
   C. 传统前后端分离
   D. H5 单页应用

176. 页面上拉触底加载更多商品时，会触发的方法是( **B** )
   A. onShareAppMessage
   B. onReachBottom
   C. onPullDownRefresh
   D. onLoadMorePage

177. 在传统小程序开发模式中，通常不需要额外投入的是( **A** )
   A. 云函数自动统计报表
   B. 数据库资源
   C. 运维保障
   D. 服务器

178. 在会员等级设计中，课程共设置了几种等级？( **A** )
   A. 4种
   B. 2种
   C. 3种
   D. 5种

179. 在微信开发者工具中，查看接口请求状态、返回数据和耗时，应主要使用调试器中的( **D** )
   A. Console
   B. AppData
   C. Memory
   D. Network

180. 每日签到成功后，用户当天的签到按钮状态应变为( **C** )
   A. 跳转商城
   B. 高亮可点
   C. 置灰不可再次点击
   D. 自动隐藏

181. 课程中，用户领取的优惠券信息主要存储在哪张表中？( **C** )
   A. 商品表
   B. 等级表
   C. 用户优惠券表
   D. 平台优惠券表

182. 课程中常规每日签到可获得多少积分？( **C** )
   A. 10分
   B. 5分
   C. 1分
   D. 0分

183. 商品列表组件接收首页传入的商品数据时，其外部属性类型应为( **B** )
   A. Number
   B. Array
   C. String
   D. Boolean

184. 商品详情页中，用于点击后分享商品给好友的按钮属性是( **A** )
   A. open-type="share"
   B. open-type="pay"
   C. open-type="navigate"
   D. open-type="contact"

185. 课程中提到，小程序相比原生 APP 的突出优势之一是( **A** )
   A. 免安装
   B. 必须下载安装
   C. 只能单机运行
   D. 传播不方便

186. 课程中提到，用于存放商品图片的是( **B** )
   A. 云函数
   B. 云存储
   C. 本地缓存
   D. 云数据库

187. 下列哪一项最符合课程中对电商小程序使用场景的描述？( **D** )
   A. 长时高频
   B. 长时低频
   C. 低频离线
   D. 短时高频

188. 商品分类功能中，商品大类与商品系列之间的关系是( **C** )
   A. 一对一
   B. 无关联
   C. 一对多
   D. 多对多

189. 商品列表分页时，用于判断数据是否已全部加载完成的额外信息是( **B** )
   A. 页面标题
   B. 商品总数
   C. 当前用户信息
   D. 商品图片数量

190. 在搜索页中，添加历史搜索记录时，最近一次搜索通常会被放在( **B** )
   A. 随机位置
   B. 数组最前面
   C. 数组末尾
   D. 数组中间

191. 课程中提到，云开发模式下主要的开发角色是( **A** )
   A. 仅前端人员
   B. 仅后端人员
   C. 仅运维人员
   D. 前端、后端、运维都必须齐备

192. 课程中，小程序端统一调用云函数的方法最终封装为( **C** )
   A. getData()
   B. run()
   C. request()
   D. fetch()

193. 会员开通时，为后续签到统计预先准备的数据会写入哪张表？( **A** )
   A. 签到统计表
   B. 商品表
   C. 用户表
   D. 优惠券表

194. 课程中，历史搜索记录采用什么方式进行管理？( **C** )
   A. 云函数
   B. 云数据库
   C. 本地缓存
   D. sessionStorage

195. 商品活动轮播图的数据中，用于控制活动展示顺序的字段是( **A** )
   A. sort
   B. banner
   C. cover
   D. label

196. 钻石会员购物时可享受的折扣是( **C** )
   A. 8折
   B. 9折
   C. 8.8折
   D. 9.5折

197. 在页面中声明 tab 页路径时，即使采用自定义 tab bar，也仍需在配置中保留的关键配置是( **A** )
   A. pagePath
   B. selectedIconPath
   C. borderStyle
   D. iconPath

198. 首页搜索框点击后首先跳转到的是( **D** )
   A. 商品详情页
   B. 购物车页
   C. 分类页
   D. 搜索中间页

199. 课程中实现自定义 tab bar 跳转页面时，使用的 API 是( **C** )
   A. wx.reLaunchTo
   B. wx.redirectTo
   C. wx.switchTab
   D. wx.navigateTo

200. 连续签到三天，除每日基础积分外，额外奖励( **B** )
   A. 10积分
   B. 20积分
   C. 50积分
   D. 30积分

201. 签到提醒功能中，课程使用的是哪种订阅消息？( **A** )
   A. 一次性订阅消息
   B. 模板消息
   C. 长期订阅消息
   D. 群发消息

202. 连续签到十天，课程中设置的额外奖励是( **D** )
   A. 20积分
   B. 100积分
   C. 30积分
   D. 50积分

203. 课程中提到，小程序体验流程中，上传开发版本后下一步通常是( **B** )
   A. 先开广告主
   B. 在公众平台设置为体验版
   C. 直接发布
   D. 删除旧版本

204. 积分商城中，100积分可以兑换哪种优惠券？( **B** )
   A. 8折优惠券
   B. 10元优惠券
   C. 20元优惠券
   D. 5元优惠券

205. 课程中，商品动态数据的后台管理主要通过什么平台完成？( **B** )
   A. 独立后台系统
   B. 内容管理平台
   C. 本地 Excel
   D. 第三方 ERP

206. 课程中会员等级基础信息是从哪里获取的？( **C** )
   A. 用户缓存
   B. 第三方接口
   C. 云数据库会员等级表
   D. 本地 JSON

207. 课程中商品价格最终展示时，价格数据是以什么单位存储的？( **A** )
   A. 分
   B. 美元
   C. 元
   D. 角

208. 1. 在会员小程序中，用户未注册时点击头像，系统通常会( **A** )
   A. 跳转到注册登录页面
   B. 打开优惠券页面
   C. 直接签到
   D. 跳转到积分商城

209. 当商户系统未能接收到支付通知时，通常应调用哪个接口确认订单支付结果？( **A** )
   A. 查询订单接口
   B. 下载对账单接口
   C. 统一下单接口
   D. 关闭订单接口

210. 为了避免重复调用用户信息查询接口，课程中采用的优化方式是( **C** )
   A. 写入云函数日志
   B. 改为同步请求
   C. 使用本地缓存
   D. 使用 tabBar 传值

211. 在本课程的支付小程序中，实现微信支付主要采用的技术方式是( **D** )
   A. 本地模拟支付
   B. 传统服务器直连
   C. 第三方支付 SDK
   D. 云开发云调用

212. 云开发模式下，用户在使用小程序时可以直接获取的信息是( **B** )
   A. 生日
   B. openID
   C. 昵称
   D. 头像

213. 同一支付订单进行分次退款时，每次重新提交退款失败后的正确做法是( **B** )
   A. 更换支付订单号
   B. 继续使用原商户退款单号
   C. 删除原订单后重建
   D. 更换退款单号

214. 微信支付“统一下单”接口的主要作用是( **D** )
   A. 查询退款状态
   B. 下载历史账单
   C. 关闭已完成订单
   D. 生成预支付交易单

215. 申请开通微信支付时，小程序主体认证必须为( **C** )
   A. 仅学生
   B. 海外主体
   C. 非个人
   D. 个人

216. 支付成功后，支付回调云函数会将订单状态更新为( **D** )
   A. 已取消
   B. 已完成
   C. 待支付
   D. 待发货

217. 商户订单号的长度要求是不超过( **C** )
   A. 24位
   B. 64位
   C. 32位
   D. 16位

218. 微信支付安全防护中，用于证明商户身份、包含商户号和公钥等信息的是( **A** )
   A. 商户 API 证书
   B. 云函数环境 ID
   C. 对账单文件
   D. 平台密钥

219. 订单确认页面中，收货地址管理采用的方式是( **D** )
   A. 自建地址表
   B. 本地缓存地址
   C. 第三方地图 SDK
   D. 微信获取用户收货地址 API

220. 订单生成后，最短多久后才能调用关单接口？( **A** )
   A. 5分钟
   B. 立即
   C. 30分钟
   D. 1分钟

221. 在课程中，用户点击商品详情页“加入购物车”后，首先会向哪张表写入数据？( **D** )
   A. 会员等级表
   B. 用户订单表
   C. 用户优惠券表
   D. 购物车表

222. 会员小程序注册登录页面中，不包含下列哪项信息填写？( **C** )
   A. 头像
   B. 昵称
   C. 收货地址
   D. 生日

223. 课程中提到，会员小程序中用户状态主要分为几种？( **D** )
   A. 5种
   B. 2种
   C. 4种
   D. 3种

224. 小程序端发起支付流程时，使用的接口是( **C** )
   A. wx.openPayment
   B. wx.pay
   C. wx.requestPayment
   D. wx.requestOrder

225. 由于购物车页面属于 tab 页面，为了保证每次切换进来数据都是最新的，课程中主要在什么生命周期获取购物车数据？( **B** )
   A. onHide
   B. onShow
   C. onReady
   D. onLoad

226. 课程中获取用户微信头像时，button 组件使用的 open-type 是( **A** )
   A. chooseAvatar
   B. getPhoneNumber
   C. chooseImage
   D. getUserInfo

227. 微信支付对账单通常建议在次日几点之后下载？( **C** )
   A. 9点
   B. 8点
   C. 10点
   D. 12点

228. 在生成订单时，为保证订单表、库存表、优惠券表、购物车表的数据一致性，课程中采用了( **D** )
   A. 定时任务
   B. 云存储回滚
   C. 本地缓存
   D. 数据库事务

229. 微信支付中，交易时间超过多久的订单无法提交退款？( **C** )
   A. 三个月
   B. 六个月
   C. 一年
   D. 两年

230. 对账单中的金额字段单位通常是( **B** )
   A. 角
   B. 元
   C. 分
   D. 厘

231. 在统一下单接口中，用于接收支付异步通知的重要配置是( **D** )
   A. 商品分类和商品库存
   B. 小程序首页路径
   C. 收货地址和备注
   D. 回调云函数名称和环境 ID

232. 用户已登录后点击“立即开通会员”，本质上是向用户信息中新增哪个标志？( **A** )
   A. 是否会员
   B. 是否管理员
   C. 是否签到
   D. 是否有优惠券

233. 课程中提到，微信零钱退款一般多久内到账？( **A** )
   A. 20分钟内
   B. 24小时内
   C. 2小时内
   D. 5分钟内

234. 下列哪种情况通常需要调用“关闭订单”接口？( **C** )
   A. 下载三个月前的对账单
   B. 用户已支付成功后再次支付
   C. 用户支付失败，需要换新订单号重新支付
   D. 订单刚生成立刻关闭

235. 1. 课程中提到，微信小游戏最终呈现在手机上的基础不包括( **A** )
   A. 页面 DOM 结构
   B. 游戏逻辑
   C. 图片资源
   D. 音频文件

236. 课程中点击选集后，从底部弹出的组件主要使用的是 TDesign 的( **D** )
   A. Tabs
   B. Cell
   C. Button
   D. Popup

237. 在 Canvas 2D 坐标系中，默认原点位于( **A** )
   A. 左上角
   B. 右上角
   C. 左下角
   D. 画布中心

238. 子弹的初始位置主要取决于( **C** )
   A. 敌机的随机坐标
   B. 背景图片坐标
   C. 玩家飞机当前坐标
   D. 分数高低

239. 在课程中，用来搭建整体页面布局的第三方组件库是( **B** )
   A. Vant Weapp
   B. TDesign
   C. Element Plus
   D. Ant Design

240. 课程中“点赞功能”主要将数据存储到( **C** )
   A. 云数据库
   B. 页面 data
   C. 本地缓存
   D. 云存储

241. 课程中敌机的初始 y 坐标设置在屏幕外侧，主要是为了( **C** )
   A. 避免加载图片
   B. 节省图片资源
   C. 让敌机从屏幕外向下进入画面
   D. 方便计算得分

242. 当玩家飞机与敌机发生碰撞后，课程中将游戏状态变量设置为( **C** )
   A. isRunning = false
   B. isPause = true
   C. isGameOver = true
   D. isFinish = true

243. 课程中定义所有精灵类共同继承的基础类名称是( **D** )
   A. Game
   B. Object
   C. Canvas2D
   D. Sprite

244. 课程中提到，微搭平台支持构建的应用类型不包括( **B** )
   A. H5
   B. 原生 Windows 桌面软件
   C. PC Web
   D. 小程序

245. 在微信小游戏项目中，作为主入口文件的是( **D** )
   A. index.js
   B. app.js
   C. main.js
   D. game.js

246. 课程中获取用户头像时，button 组件设置的 open-type 是( **C** )
   A. chooseImage
   B. getPhoneNumber
   C. chooseAvatar
   D. getUserInfo

247. 在微搭平台中，开发小程序应用首先需要具备的是( **B** )
   A. 微信个人号
   B. 腾讯云账号
   C. GitHub 账号
   D. 企业邮箱

248. 在自定义组件中，用于接收外部传入数据的配置项是( **C** )
   A. methods
   B. data
   C. properties
   D. observers

249. 课程中背景音乐播放时，为了持续循环，需要设置的属性是( **A** )
   A. loop
   B. preload
   C. autoplay
   D. muted

250. 为了实现背景滚动效果，课程中至少创建了几张背景图进行衔接显示？( **D** )
   A. 4张
   B. 3张
   C. 1张
   D. 2张

251. 课程中“连续播放”功能开启后，下一集自动播放的触发时机是( **C** )
   A. 视频暂停时
   B. 视频开始播放时
   C. 视频播放结束时
   D. 页面返回时

252. 腾讯云微搭属于哪一类开发平台？( **A** )
   A. 高性能低代码开发平台
   B. 数据库管理平台
   C. 服务器运维平台
   D. 纯代码开发平台

253. 课程中短剧小程序共设计了几个 tab 页面？( **B** )
   A. 5个
   B. 3个
   C. 2个
   D. 4个

254. 在小游戏中获取 Canvas 2D 上下文时，课程中采用的方式是( **A** )
   A. 直接使用全局 canvas 对象获取 context
   B. 通过 DOM 查询 canvas 元素
   C. 通过 Page 实例获取
   D. 通过 wx.createSelectorQuery() 获取

255. 从基础库 2.24.4 起，课程中获取昵称时要求 input 外层嵌套( **A** )
   A. form
   B. scroll-view
   C. navigator
   D. video

256. 课程中用于操作 video 组件、实现播放暂停和倍速等功能的对象是( **D** )
   A. video event
   B. video player
   C. video manager
   D. video context

257. 在微信开发者工具中新建微信小游戏时，课程中选择的官方模板是( **C** )
   A. 贪吃蛇
   B. 俄罗斯方块
   C. 飞机大战
   D. 消消乐

258. 课程中“剧场”页面下方的短剧展示采用的是( **C** )
   A. 瀑布流布局
   B. 双列布局
   C. 三栏式布局
   D. 单列布局

259. 视频播放组件中，用于指定视频资源地址的必填属性是( **C** )
   A. file
   B. path
   C. src
   D. url

260. 在“追剧”页面中，上方板块主要展示的是( **C** )
   A. 我的积分
   B. 我的收藏
   C. 最近观看
   D. 最热剧集

261. 实现视频倍速播放时，课程中调用的方法是( **B** )
   A. setRate()
   B. playbackRate()
   C. speedPlay()
   D. changeSpeed()

262. 对于前端开发者，课程中提到微搭提供的重点能力之一是( **A** )
   A. 数据源 API 与自定义代码模块
   B. 芯片驱动开发
   C. 纯离线数据库引擎
   D. 机械设计建模

263. 微信小游戏运行原生 JavaScript 时，依赖的宿主环境是( **B** )
   A. 浏览器 DOM 环境
   B. 微信提供的运行环境
   C. Vue 组件环境
   D. Node.js 服务端环境

264. 课程中为玩家飞机添加拖动控制时，主要监听的事件对象绑定在( **D** )
   A. window
   B. document
   C. audio
   D. canvas

265. 1. 课程中，为了实现点击按钮后隐藏一段文字，首先创建的是哪种类型的自定义变量？( **A** )
   A. 布尔值
   B. 数值
   C. 数组
   D. 字符串

266. 从课程内容看，会员通常更偏向于( **C** )
   A. 只存在于第三方平台的访客
   B. 仅仅是浏览用户
   C. 已经产生交易行为的高粘度客户
   D. 完全陌生的潜在用户

267. 银行卡包项目中，银行卡号识别主要调用的是哪类能力？( **A** )
   A. OCR 文字识别
   B. 内容安全检测
   C. 地图定位
   D. 语音识别

268. 银行卡包项目中，用来存储银行卡类型的字段是( **C** )
   A. cardName
   B. type
   C. tab
   D. bankType

269. 课程中提到，小程序正式发布后，下一步通常需要进行( **B** )
   A. 删除应用版本
   B. 提交审核
   C. 关闭控制台
   D. 重新绑定账号

270. 储值型会员体系最典型的特点是( **C** )
   A. 用户先支付会费成为会员
   B. 主要依赖积分升级
   C. 用户预先储值后再消费
   D. 依赖跨平台生态合作

271. 相册分享小程序中，用来保存当前用户图片列表的字段是( **A** )
   A. photos
   B. images
   C. albumList
   D. files

272. 在私域价值公式中，反映用户消费水平的指标是( **A** )
   A. 客单价
   B. 用户数量
   C. 用户粘性
   D. 用户转化率

273. 银行卡包首页渲染列表数据时，页面 data 中使用的数组变量是( **B** )
   A. list
   B. cards
   C. banks
   D. bankList

274. 在微搭控制台中，若要创建一个没有内容的小程序，课程中选择的是( **D** )
   A. 从模板导入
   B. 一键发布
   C. 快速克隆
   D. 从空白创建

275. 新闻管理页中，默认的排序方式是根据创建时间进行( **C** )
   A. 随机排序
   B. 升序
   C. 降序
   D. 手动排序

276. 课程中的新闻小程序，新增新闻记录最终保存到哪个集合中？( **A** )
   A. news
   B. photos
   C. users
   D. cards

277. 在相册小程序中，获取用户唯一标识 openID 主要借助( **C** )
   A. 本地缓存
   B. 云存储下载
   C. 云函数
   D. 云数据库查询

278. 在课程给出的私域运营链路中，最终目标更偏向于( **B** )
   A. 只做内容分发
   B. 用户复购提升
   C. 单纯涨粉
   D. 单次曝光

279. 下列哪一项更符合课程中“公域流量”的例子？( **B** )
   A. 企业微信群
   B. 淘宝、京东、小红书等平台流量
   C. 公众号粉丝
   D. 品牌小程序会员

280. 相册小程序中，长按图片后弹出的操作菜单不包括( **A** )
   A. 编辑标题
   B. 操作菜单
   C. 删除图片
   D. 下载到本地

281. 课程中提到，上传文件到云存储成功后最重要的返回标识之一是( **D** )
   A. appId
   B. secretKey
   C. tempUrl
   D. fileID

282. 课程中提到，付费型会员体系的核心特点是( **D** )
   A. 通过预存金额锁客
   B. 通过社群免费裂变
   C. 通过线下充值获得积分
   D. 通过支付一定费用获取更高级权益

283. 课程中指出，客户与会员的关系是( **A** )
   A. 客户并不等同于会员
   B. 客户一定等于会员
   C. 二者完全没有关系
   D. 会员一定不属于客户

284. 新闻小程序详情页获取某一条新闻详情时，主要通过哪个参数定位记录？( **C** )
   A. title
   B. createName
   C. id
   D. subtitle

285. 新闻管理页中，搜索功能主要是基于哪个字段进行匹配？( **A** )
   A. title
   B. subtitle
   C. content
   D. createTime

286. 在微搭中，为按钮绑定点击行为主要是在右侧配置面板的哪个属性区域完成？( **B** )
   A. 样式
   B. 事件
   C. 布局
   D. 数据

287. 相册小程序中，点击图片后进入预览功能主要调用的是( **B** )
   A. wx.openDocument
   B. wx.previewImage
   C. wx.showImage
   D. wx.previewMedia

288. 课程中，在微搭里打开微信开发者工具预览小程序的入口是( **B** )
   A. 素材库
   B. 顶部菜单栏三个点中的“小程序微信IDE预览”
   C. 数据源管理
   D. 页面样式设置

289. 生态型会员体系更强调( **A** )
   A. 跨平台、跨业务资源整合
   B. 只做线下发券
   C. 只做积分兑换
   D. 单一门店充值

290. 课程中提到，成长型会员体系的核心目标是( **C** )
   A. 联名共生
   B. 预售锁定
   C. 积分驱动
   D. 付费驱动

291. 在微搭平台中，若要连接第三方数据库，课程中提到可以使用( **B** )
   A. 主题编辑器
   B. 数据连接器
   C. 轮播图组件
   D. 页面克隆

292. 课程中提到，私域流量相较于公域流量的一个显著优势是( **A** )
   A. 可被企业多次重复利用
   B. 用户无法反复触达
   C. 必须持续付费购买
   D. 只能做品牌曝光，不能做转化

293. 课程中提到，私域体系搭建时首先要做的是( **A** )
   A. 明确企业希望通过私域实现的目标
   B. 先搭建所有社群
   C. 立即投放广告
   D. 先开发 APP

294. 银行卡包项目中，用于实现银行卡 OCR 识别的云函数名称是( **C** )
   A. getCard
   B. readBank
   C. scan card
   D. cardInfo

295. 在 IDE 中预览微搭生成的小程序前，课程中提到需要先完成的一项关键操作是( **D** )
   A. 购买数据库实例
   B. 配置 CDN 域名
   C. 开通企业微信
   D. 绑定小程序 AppID

296. 课程中提到，在页面上添加轮播图时，应先从组件区搜索( **A** )
   A. 轮播图
   B. 地图
   C. 表格
   D. 图表

297. 课程中给出的私域价值公式是( **A** )
   A. 私域价值=用户数量×用户粘性×用户转化率×客单价
   B. 私域价值=曝光量×点击率
   C. 私域价值=粉丝量×点赞量
   D. 私域价值=用户数量×广告预算

298. 课程中对“私域流量”的核心定义是( **A** )
   A. 企业能够直接连接并低成本反复触达的流量
   B. 只能依赖搜索引擎获取的流量
   C. 只能在线下门店获取的流量
   D. 通过广告平台一次性购买的流量

299. 在微搭页面编辑器中，左上角用于显示组件层级结构的区域是( **B** )
   A. 开发工具栏
   B. 大纲树
   C. 页面管理栏
   D. 事件面板


## 二、多选题汇总（共 150 题）

1. 接入微信支付前，课程中提到通常需要具备的条件有( **ABCD** )
   A. 小程序与商户绑定  B. 配置支付密钥和证书  C. 商户号  D. 企业小程序 AppID

2. 微信小程序登录的完整流程中，可能涉及的内容有( **ABCD** )
   A. wx.login 获取 code  B. 后台换取 openid 等凭证  C. wx.request 调用后台接口  D. 前端缓存登录态

3. 关于文件上传接口 wx.uploadFile，下列说法正确的是( **ABCD** )
   A. 需要指定本地文件路径  B. 需要指定上传服务器地址  C. 需要设置文件对应的 name  D. 上传成功后可在 success 回调中处理业务

4. 课程中提到，较新版本下获取用户相关信息的方式包括( **CD** )
   A. 一律使用 wx.getUserInfo  B. 一律使用 wx.getUserProfile  C. 通过输入框填写昵称  D. 通过按钮选择微信头像

5. 下列哪些文件类型是课程中提到 wx.openDocument 支持打开的?( **ABCD** )
   A. pdf  B. xls  C. ppt  D. doc

6. 课程中提到，获取用户地理位置前需要授权的原因包括( **ABD** )
   A. 满足法律法规要求  B. 保护用户隐私  C. 优化个性化服务  D. 保障用户知情权

7. 关于地理位置相关能力，下列说法正确的是( **ABCD** )
   A. 获取位置前通常要完成授权配置  B. 可通过 openLocation 查看位置  C. 可通过 chooseLocation 选择位置  D. 页面中可借助 map 组件渲染位置

8. 关于微信小程序 AI 推理能力，下列说法正确的是( **ABCD** )
   A. 使用前对基础库和微信版本有要求  B. 常见流程包括获取环境、创建会话、加载模型、运行推理  C. 可应用于推荐、翻译、智能客服、图像识别等场景  D. 需要在 AI 平台注册账号并创建应用/模型

9. 下列属于小程序本地缓存常见操作的是( **ABCD** )
   A. 删除指定缓存  B. 写入缓存  C. 读取缓存  D. 清空全部缓存

10. 关于同步接口和异步接口，下列说法正确的是( **ABCD** )
   A. 异步接口不必等待当前任务完成  B. 同步接口按顺序执行  C. 不带 Sync 的一般为异步接口  D. 带 Sync 后缀的一般为同步接口

11. 微信客户端作为小程序的“宿主环境”，主要为小程序的正常运行提供了哪些方面的底层支持？( **ABCD** )
   A. 渲染层和逻辑层的通信模型
   B. 小程序的启动和渲染运行机制
   C. 丰富的UI基础组件
   D. 调用底层能力的各类API(如定位、支付)

12. 当使用普通的 navigateTo 方式从页面 A 跳转到页面 B 时，关于这两个页面的生命周期变化，下列描述正确的有？( **BC** )
   A. 页面A会被销毁，触发 onUnload
   B. 页面A仅是被隐藏进入页面栈，触发 onHide
   C. 页面B会被初始化并显示，触发 onLoad 和 onShow
   D. 页面A和页面B都会触发 onLaunch

13. 在使用 setData 方法更新数据时，为了保证小程序的性能并避免潜在的 Bug，应该遵循以下哪些原则？( **ABC** )
   A. 绝对不能使用 this.data 直接对变量赋值来更新视图
   B. 尽量避免一次性设置过多的数据(受最大值限制)
   C. 避免过于频繁地调用 setData，尽量将多个赋值操作合并在一次调用中
   D. 推荐将暂时不用的变量通过 setData 设置为 undefined

14. 关于条件渲染中的 wx:if 和 <block> 标签，下列说法正确的有？( **ABCD** )
   A. <block> 标签并不是一个真正的组件，仅仅是一个包装元素
   B. <block> 标签本身不会在页面上做任何的渲染输出
   C. 可以将 wx:if 指令添加在 <block> 标签上，用来控制内部多块元素的渲染
   D. 当 wx:if 的判断条件为 false 时，其控制的代码块元素会被直接销毁(不渲染)

15. 在小程序的事件体系中，事件被分为了“冒泡事件”和“非冒泡事件”。下列事件中，属于“冒泡事件”(触发后会向父节点传递)的有？( **AB** )
   A. tap (手指触摸点击)
   B. longpress (手指长按)
   C. input (输入框键盘输入)
   D. submit (表单提交)

16. 在微信小程序的目录结构中，一个标准的页面文件夹通常包含哪几种后缀的文件？( **ABCD** )
   A. .js
   B. .json
   C. .wxml
   D. .wxss

17. 下列属于微信小程序中“视图容器类组件”(主要用于页面布局和视图展示)的有？( **ABC** )
   A. view
   B. scroll-view
   C. swiper
   D. text

18. 在使用 navigator 组件实现页面跳转时，open-type 属性支持以下哪些跳转方式？( **ABCD** )
   A. navigate
   B. redirect
   C. switchTab
   D. reLaunch

19. 在配置原生的 tabBar 时，list 数组里的每一项(item)都可以设置哪些关键属性？( **ABCD** )
   A. pagePath
   B. text
   C. iconPath
   D. selectedIconPath

20. 关于微信小程序中数据的管理和获取，下列说法正确的有？( **ABC** )
   A. 页面内部定义的数据存放在js文件的 data 对象中，通过 this.data 获取
   B. 全局共享的数据存放在 app.js 的 globalData 中，通过 getApp().globalData 获取
   C. 外部工具类js文件中定义的方法，可以通过 module.exports 暴露出去
   D. 页面的工具类 js 文件通过 @import 语法进行加载引入

21. 新增一个小程序页面的方式有以下哪几种？( **AB** )
   A. 直接在 app.json 的 pages 数组中增加新页面的路径，开发者工具会自动生成对应文件
   B. 直接在 pages 文件夹下新建一个文件夹，并在里面新建对应的 wxml 等页面文件
   C. 必须通过向微信官方提交页面增加申请才能创建
   D. 只能通过在 project.config.json 中配置来增加页面

22. 关于小程序合法域名配置，下列说法正确的是( **ACD** )
   A. 一般应配置子域名而不是父域名
   B. 可以直接使用 localhost 作为正式请求域名
   C. 域名需支持 https
   D. 域名需完成 ICP 备案

23. 关于页面事件处理函数，下列说法正确的是( **ABCD** )
   A. 一般更建议使用页面级局部配置
   B. 上拉触底可通过 onReachBottomDistance 配置触发距离
   C. 下拉刷新监听函数是 onPullDownRefresh
   D. 下拉刷新可全局开启，也可局部开启

24. 关于 GET 和 POST 请求，下列说法正确的是( **ABCD** )
   A. GET 常用于获取数据
   B. GET 通过 URL 传参，安全性相对较低
   C. POST 更适合提交数据
   D. POST 更适合传递大量数据

25. 课程中提到的用户分享相关接口或事件包括( **ABD** )
   A. onAddToFavorites
   B. onShareTimeline
   C. onShareQQZone
   D. onShareAppMessage

26. 下列属于小程序组件常用公共属性的是( **ABCD** )
   A. style
   B. id
   C. class
   D. data-*

27. 在 wx.request 中，课程提到的常见参数有( **ABCD** )
   A. data
   B. method
   C. url
   D. header

28. 下列属于课程中提到的小程序网络请求相关 API 的是( **ACD** )
   A. wx.request
   B. wx.connectSocket
   C. wx.uploadFile
   D. wx.downloadFile

29. 关于小程序自定义属性 data-*，下列说法正确的是( **ABC** )
   A. * 位置可以自定义名称
   B. 获取时常通过 event.currentTarget.dataset
   C. 可用于给组件传递额外参数
   D. 只能传递数字，不能传字符串

30. 下列哪些 API 可用于提升网络请求过程中的用户体验？( **ABCD** )
   A. wx.showModal
   B. wx.showNavigationBarLoading
   C. wx.showToast
   D. wx.showLoading

31. 课程中介绍的小程序页面传参方式包括( **ABC** )
   A. 全局数据传参
   B. 页面栈传参
   C. 事件结合 URL 传参
   D. 关系型数据库传参

32. 下列属于课程中提到的常用组件生命周期的是( **ABD** )
   A. detached
   B. attached
   C. onLoad
   D. created

33. 下列关于自定义组件和页面的区别，正确的是( **ABC** )
   A. 页面通过 Page() 注册
   B. 组件通过 Component() 注册
   C. 组件 json 中需声明 component: true
   D. 组件和页面的生命周期定义位置完全相同

34. 关于插槽 slot，下列说法正确的是( **ABCD** )
   A. 多插槽必须命名
   B. 单插槽一般不必命名
   C. 多插槽场景下需要开启对应配置
   D. 可以让外部向组件传入标签内容

35. 关于组件所在页面的生命周期，下列说法正确的是( **BCD** )
   A. 与组件自身 lifetimes 完全相同
   B. 组件依赖页面存在
   C. 可在 pageLifetimes 中定义
   D. 常见的有 show 和 hide

36. 关于组件样式隔离，下列说法正确的是( **ABC** )
   A. 可以防止页面样式和组件样式互相干扰
   B. 可以防止不同组件之间样式互相污染
   C. 开发时应尽量避免使用标签选择器和 id 选择器
   D. 全局 app.wxss 对组件默认生效

37. 课程中提到的组件通信方式包括( **ABCD** )
   A. 子组件通过事件向父组件传值
   B. 父组件通过属性向子组件传值
   C. 无关联组件可借助 globalData 传值
   D. 无关联组件可借助 storage 传值

38. 关于 properties 和 data，下列说法正确的是( **ABD** )
   A. data 用于定义组件内部数据
   B. 二者的用途不同，应区分使用
   C. properties 和 data 没有区别
   D. properties 用于接收外部传值

39. 下列属于课程中提到的组件化开发优势的是( **ABCD** )
   A. 支持团队并行开发
   B. 代码复用
   C. 方便后期维护
   D. 代码解耦

40. 关于 behaviors，下列说法正确的是( **ABCD** )
   A. 引入后相关内容会合并到组件中
   B. 可用于组件之间代码共享
   C. 可以包含数据和方法
   D. 可以包含生命周期

41. 关于 observers 数据监听，下列说法正确的是( **ACD** )
   A. 可监听深层对象字段
   B. 只能监听字符串，不能监听对象
   C. 可监听所有数据变化
   D. 可监听普通数据

42. 关于骨架屏，课程中提到的实现方式包括( **ABC** )
   A. 手动定制页面
   B. 使用模板判断加载状态后切换显示
   C. 借助工具组件渲染
   D. 使用小程序自带功能生成

43. 课程中提到，小程序性能优化的意义包括( **BCD** )
   A. 降低维护成本
   B. 增强核心竞争力
   C. 提高用户满意度和留存率
   D. 提升用户体验

44. 关于分包，下列说法正确的是( **ABCD** )
   A. 分包有助于多团队协作开发
   B. 分包分为主包和分包
   C. 默认启动页面必须在主包中
   D. 用户进入某个分包页面时，客户端会下载对应分包

45. 下列属于课程中提到的启动性能优化方案的是( **BCD** )
   A. 增加无用组件
   B. 代码注入优化
   C. 首屏渲染优化
   D. 优化代码包体积

46. 关于资源加载优化，课程中提到的方案包括( **ABCD** )
   A. 图片压缩
   B. 图片懒加载
   C. 将图片托管到 CDN
   D. 预先指定图片尺寸

47. 关于云数据库条件查询，课程中提到的能力包括( **ABCD** )
   A. 指定字段返回
   B. 数组包含查询
   C. 数组不包含查询
   D. 地理位置查询

48. 关于云调用，下列说法正确的是( **ABCD** )
   A. 是基于云函数使用小程序开放接口的能力
   B. 在一定场景下无需手动换取 access_token
   C. 调用前通常要先确认接口是否支持云调用
   D. 支持服务端调用等场景

49. 课程中提到的云开发核心能力包括( **BCD** )
   A. 云托管
   B. 云函数
   C. 云数据库
   D. 云存储

50. 课程中提到，云函数模板里的常见内容包括( **ABCD** )
   A. context 参数
   B. wx-server-sdk
   C. event 参数
   D. exports.main 入口函数

51. 关于“云代办”实战功能，课程中实现或讲解到的内容包括( **ABCD** )
   A. 设置位置并导航
   B. 添加待办
   C. 上传图片
   D. 查看待办和详情

52. 关于云开发控制台，下列说法正确的是( **ABCD** )
   A. 可管理云函数及查看日志监控
   B. 可查看云资源总体使用情况
   C. 可查看运营分析数据
   D. 可管理数据库集合和权限

53. “云代办”小程序中，课程设计的任务字段包括( **ABCD** )
   A. image
   B. title
   C. location / locationGPS
   D. status

54. 关于云存储，课程中提到的功能包括( **BCD** )
   A. 文件搜索
   B. 文件上传
   C. 文件删除、移动、下载
   D. 通过 fileID 在组件中展示资源

55. 课程中演示过的云调用实战案例包括( **ACD** )
   A. 发送订阅消息
   B. 获取文章列表 RSS
   C. 图片内容安全识别
   D. 生成小程序码

56. 关于云函数的创建与使用，下列说法正确的是( **ABCD** )
   A. 可在工具中右键新建 Node.js 云函数
   B. 云函数通常需要上传并部署后才能调用
   C. 需要先配置 cloudfunctionRoot
   D. 小程序端可通过 wx.cloud.callFunction 调用

57. 1. 关于在云函数中使用第三方 npm 包，课程中提到的方式包括( **ABC** )
   A. 使用 Node.js 环境运行
   B. 可借助现成工具库加速开发
   C. 云端安装依赖
   D. 全量上传

58. 课程中演示过的云调用实战包括( **ABD** )
   A. 生成小程序码
   B. 发送订阅消息
   C. 获取文章 RSS
   D. 图片内容安全识别

59. 云代办小程序中的核心功能包括( **ABCD** )
   A. 新增任务
   B. 上传图片附件
   C. 查看位置并导航
   D. 查看任务

60. 发送订阅消息时，课程中提到需要的关键内容包括( **ABCD** )
   A. 模板 ID
   B. 推送内容 data
   C. 接收者 openID
   D. 跳转页面配置

61. 发送邮件示例中，mail 对象包含的常见字段有( **ABCD** )
   A. html / text 内容
   B. subject
   C. from
   D. to

62. 云代办小程序设计的主要字段包括( **ABCD** )
   A. title
   B. status
   C. image
   D. location / locationGPS

63. 课程中用户管理示例的主要流程包括( **ABCD** )
   A. 完成数据库保存
   B. 写入 users 集合
   C. 通过按钮获取用户信息
   D. 读取 event.detail.userInfo

64. 课程中提到，云函数中可使用的资源和服务包括( **BCD** )
   A. 第三方数据库
   B. 云存储
   C. 第三方服务
   D. 云数据库

65. 课程中讲到的云函数典型操作包括( **ABCD** )
   A. 删除数据库数据
   B. 查询数据库数据
   C. 更新数据库数据
   D. 新增数据库数据

66. 1. 发送邮件示例中，mail 对象包含的常见字段有( **ABCD** )
   A. html / text 内容
   B. subject
   C. from
   D. to

67. 云开发控制台中常见的模块包括( **ABCD** )
   A. 存储与云函数
   B. 运营分析
   C. 概览
   D. 数据库

68. 在小程序端调用云函数时，课程中传入的常见内容包括( **ABCD** )
   A. 云函数名称
   B. data 参数
   C. fail 回调
   D. success 回调

69. 关于云数据库权限，课程中介绍的常见权限有( **ABCD** )
   A. 所有人可读
   B. 所有人不可读写
   C. 所有人可读，仅创建者可写
   D. 仅创建者可读写

70. 课程中提到的云开发优势包括( **ABCD** )
   A. 无需搭建服务器
   B. 可免登录免鉴权调用部分能力
   C. 支持多端复用
   D. 按量计费

71. 关于云函数，课程中提到的常见内容包括( **ABCD** )
   A. event 参数
   B. context 参数
   C. wx-server-sdk
   D. 入口函数 exports.main

72. 云存储提供的常见能力包括( **ABCD** )
   A. 删除
   B. 上传
   C. 搜索
   D. 下载

73. 课程中提到，云文件 fileID 可直接用于哪些组件展示资源？( **ACD** )
   A. 视频
   B. 文本框
   C. 图片
   D. 音频

74. 传统小程序开发模式通常涉及的额外投入包括( **ABCD** )
   A. 运维保障
   B. 服务器部署
   C. 存储资源
   D. 数据库资源

75. 1. 在小程序端调用云函数时，课程中传入的常见内容包括( **ABCD** )
   A. fail 回调
   B. data 参数
   C. 云函数名称
   D. success 回调

76. 关于数据库权限，课程中提到的常见权限有( **ABCD** )
   A. 所有人不可读写
   B. 仅创建者可读写
   C. 所有人可读写
   D. 所有人可读，仅创建者可写

77. 关于云函数模板，课程中提到的常见内容包括( **ABCD** )
   A. context 参数
   B. event 参数
   C. wx-server-sdk
   D. exports.main 入口函数

78. 传统开发模式中常见的额外投入包括( **ABCD** )
   A. 服务器部署
   B. 数据库资源
   C. 运维保障
   D. 存储资源

79. 云开发控制台中的常见模块包括( **ABCD** )
   A. 数据库
   B. 存储与云函数
   C. 概览
   D. 运营分析

80. 课程中提到，云文件 fileID 可直接用于哪些资源展示场景？( **ABCD** )
   A. 图片
   B. 小程序标签组件展示
   C. 视频
   D. 音频

81. 1. 云代办小程序中，课程中设计或实现的功能包括( **ABCD** )
   A. 查看任务和详情
   B. 上传图片附件
   C. 新增任务
   D. 查看地点并导航

82. 在小程序端调用云函数时，常见配置包括( **ABCD** )
   A. success
   B. fail
   C. data
   D. name

83. 课程中演示过的云调用实战包括( **ACD** )
   A. 图片内容安全识别
   B. 发送邮件
   C. 生成小程序码
   D. 发送订阅消息

84. 课程中提到，云函数中可进行的数据库操作包括( **ABCD** )
   A. 查询
   B. 删除
   C. 新增
   D. 更新

85. 关于在云函数中使用第三方 npm 包，课程中提到的特点包括( **ABCD** )
   A. 可选择云端安装依赖
   B. 可在 Node.js 环境中安装
   C. 可借助现成工具库提升开发效率
   D. 可选择全量上传

86. 课程中提到的优惠券类型包括( **ABCD** )
   A. 折扣优惠券
   B. 满减优惠券
   C. 平台优惠券
   D. 用户优惠券

87. 商品搜索结果页中，课程中提到支持的筛选或排序方式包括( **ABCD** )
   A. 综合排序
   B. 价格区间筛选
   C. 价格升序
   D. 价格降序

88. “我的优惠券”页面中，优惠券状态分为( **ACD** )
   A. 已使用
   B. 已冻结
   C. 已失效
   D. 可使用

89. 商品列表分页加载功能中，课程提到的配套能力包括( **ABCD** )
   A. 获取商品总数
   B. 上拉触底加载
   C. 刷新重试
   D. Load More 状态提示

90. 内容管理平台中，课程提到的主要菜单包括( **ABCD** )
   A. 内容集合
   B. Web Hook
   C. 项目设置
   D. 内容模型

91. 会员开通后，页面上会显示的信息包括( **ABCD** )
   A. 会员积分
   B. 会员卡信息
   C. 签到有礼
   D. 会员等级

92. 关于签到提醒功能，下列说法正确的是( **ABC** )
   A. 首次开启会询问用户是否允许接收提醒
   B. 课程中使用的是一次性订阅消息
   C. 可结合定时触发云函数推送提醒
   D. 用户关闭订阅后仍一定能收到提醒

93. 课程中商品详情页涉及的数据表包括( **ABCD** )
   A. 商品评价表
   B. 商品详情表
   C. 商品规格表
   D. 商品库存表

94. 关于历史搜索管理，课程中实现了哪些操作？( **ABCD** )
   A. 去重处理
   B. 清空全部历史记录
   C. 新增历史记录
   D. 删除指定记录

95. 关于搜索功能，课程中提到可触发跳转到搜索结果页的方式有( **ABCD** )
   A. 点击热门搜索
   B. 点击历史搜索
   C. 输入关键字后点击搜索
   D. 输入关键字后按回车

96. 每日签到功能中，签到时会涉及到更新的表包括( **ABD** )
   A. 用户表
   B. 积分流水表
   C. 会员等级表
   D. 签到统计表

97. 相较于传统开发模式，课程中提到云开发模式的优势包括( **ABCD** )
   A. 无需自行搭建服务器
   B. 可通过内容管理平台管理数据
   C. 支持按量计费
   D. 云函数可多端复用

98. 课程中商品详情页实现的主要功能包括( **ABCD** )
   A. 商品图片轮播与预览
   B. 商品评价展示与统计
   C. 富文本商品描述展示
   D. 商品规格选择

99. 课程中会员小程序的核心功能包括( **ABCD** )
   A. 积分系统
   B. 会员开通
   C. 用户注册登录
   D. 优惠券中心

100. 课程中介绍的商城首页主要功能包括( **ABCD** )
   A. 商品列表
   B. 底部导航栏
   C. 商品活动轮播图
   D. 搜索入口

101. 注册登录页面中，用户可通过哪些方式完善头像信息？( **BCD** )
   A. 自动抓取身份证照片
   B. 拍照上传
   C. 从相册选择
   D. 选择微信头像

102. 课程中提到，电商小程序适合发展的原因包括( **ABCD** )
   A. 自带支付、客服、物流等能力
   B. 社交传播方便
   C. 微信内可直接打开和转发
   D. 免安装

103. 课程中提到的小程序运营推广方式包括( **ABCD** )
   A. 设置分享奖励
   B. 公众号关联小程序
   C. 线下二维码推广
   D. 开通广告主

104. 关于微信支付安全防护，课程中提到的关键概念包括( **ABCD** )
   A. 微信支付平台证书
   B. 数字签名
   C. API v3 密钥
   D. 商户 API 证书

105. 申请微信支付开通时，课程中提到个体商户通常需要准备的材料包括( **ABC** )
   A. 营业执照
   B. 法人身份证
   C. 对公银行账户或法人对私账户
   D. 组织机构代码证

106. 统一下单接口中，课程提到的必需或关键参数包括( **ABCD** )
   A. 随机字符串
   B. 商户订单号
   C. 商品描述
   D. 终端 IP

107. 下列哪些情况适合调用“查询订单”接口？( **ABCD** )
   A. 需要确认最终支付结果
   B. 支付接口返回系统错误
   C. 支付接口返回未知交易状态
   D. 商户未收到支付通知

108. 课程中提到，使用云开发对接微信支付的优势包括( **ABCD** )
   A. 可用云函数接收支付和退款回调
   B. 相对更安全高效
   C. 不依赖第三方模块
   D. 无需关心证书签名细节

109. “我的订单”页面中，课程中提到的典型操作包括( **ABCD** )
   A. 待付款或待发货订单可取消
   B. 待收货订单可确认收货
   C. 待付款订单可付款
   D. 已完成订单可评价或申请售后

110. 在线客服功能中，课程中讲到的能力包括( **ABCD** )
   A. 将用户消息转发至客服系统
   B. 添加人工客服进行回复
   C. button 设置 open-type="contact" 唤起客服
   D. 云函数自动回复文本消息

111. 关于退款接口，课程中提到的注意事项包括( **ABCD** )
   A. 分次退款每次都应使用不同退款单号
   B. 退款总金额不能超过原订单金额
   C. 交易超过一年不能退款
   D. 单笔交易支持分多次退款

112. 课程中会员权益主要体现在以下哪些方面？( **ABCD** )
   A. 生日礼品
   B. 会员折扣
   C. 会员专属活动
   D. 会员积分

113. 微信开发者工具调试器可用于( **ABCD** )
   A. 调试 JS 代码
   B. 查看页面结构
   C. 修改页面样式
   D. 查看组件数据

114. 订单确认页面中，课程实现的功能包括( **ABCD** )
   A. 优惠券选择
   B. 收货地址选择
   C. 实付金额动态计算
   D. 订单备注填写

115. 课程中购物车商品数据写入时，包含的信息有( **ABCD** )
   A. 用户 openID
   B. 购买数量
   C. 商品 ID
   D. 规格组合 ID

116. 课程中提到，构成一个微信小游戏的核心要素包括( **ABCD** )
   A. 游戏规则与玩法
   B. 音频文件
   C. 图片资源
   D. 游戏逻辑

117. 课程中音效资源管理器负责处理的音频类型包括( **ACD** )
   A. 爆炸音效
   B. 订单支付提示音
   C. 背景音乐
   D. 子弹发射音效

118. 课程中提到，数据源管理页面可完成的操作包括( **ABCD** )
   A. 使用开放服务 API
   B. 创建数据连接器
   C. 管理数据
   D. 添加自定义 API

119. 课程中介绍的微信小游戏项目目录中，常见内容包括( **ABCD** )
   A. audio 文件夹
   B. game.json
   C. images 文件夹
   D. game.js

120. 关于微搭页面设计，课程中演示过的操作包括( **ABCD** )
   A. 新建页面
   B. 重命名页面
   C. 删除页面
   D. 复制/克隆页面

121. 课程中短剧小程序“详情页”支持的功能包括( **ABCD** )
   A. 点赞
   B. 倍速播放
   C. 追剧
   D. 横竖屏切换观看

122. 课程中按钮点击事件可绑定的动作包括( **ABCD** )
   A. 查询数据
   B. 打开弹窗
   C. 触发流程
   D. 调用自定义 JS 方法

123. 课程中基础精灵类 Sprite 的公共属性主要包括( **ABCD** )
   A. 坐标位置
   B. 宽高
   C. 图片对象
   D. 是否显示

124. 课程中拆分通用自定义组件的原因包括( **ABCD** )
   A. 提高复用性
   B. 便于统一维护
   C. 多个页面共用相似条目
   D. 页面布局较复杂

125. 课程中提到 TDesign 常用到的组件包括( **ABCD** )
   A. Cell
   B. Popup
   C. Tabs
   D. Image

126. 课程中游戏结束后会进行的处理包括( **ABCD** )
   A. 显示结束面板
   B. 提供重新开始按钮
   C. 清除敌机和子弹生成计时器
   D. 暂停背景音乐

127. 课程中“最近观看”功能的实现涉及( **ABCD** )
   A. 点击条目时写入缓存
   B. 播放某集时更新 current number
   C. 计算观看百分比
   D. 暂停视频时更新播放时间

128. Canvas 2D 常用 API 在课程中提到的包括( **ABCD** )
   A. drawImage
   B. fillText
   C. fillRect
   D. getContext

129. 课程中“追剧功能”缓存的数据字段包括( **ABCD** )
   A. 影视剧 ID
   B. 当前观看时间
   C. 当前观看集数
   D. 总集数

130. 课程中提到，微搭针对小程序开发者提供的专有能力包括( **ABCD** )
   A. 小程序分包
   B. 小程序专有组件
   C. 小程序快捷注册
   D. 微信工具箱

131. 在微搭左侧导航栏中，课程中提到的主要入口包括( **ABCD** )
   A. 素材与应用设置
   B. 页面设计
   C. 数据源
   D. 工作流

132. 课程中玩家飞机触摸控制相关的监听事件包括( **ABD** )
   A. touchmove
   B. touchstart
   C. touchcancel
   D. touchend

133. 课程中提到，在微搭平台中完成小程序开发后，后续流程包括( **ABCD** )
   A. 绑定已有小程序或注册新小程序
   B. 提交审核
   C. 发布正式版本
   D. 微信 IDE 预览调试

134. video context 对象可实现的功能包括( **ABCD** )
   A. playbackRate 倍速播放
   B. pause 暂停
   C. seek 跳转到指定位置
   D. play 播放

135. video 组件常用的基础播放属性包括( **ABCD** )
   A. controls
   B. muted
   C. autoplay
   D. loop

136. 课程中提到的会员体系设计趋势包括( **ABCD** )
   A. 可持续发展的绿色会员制度
   B. 数据驱动的会员制度
   C. 跨界合作的会员制度
   D. 线上线下融合并加入社交元素

137. 银行卡 OCR 识别功能的整体流程包括( **ABCD** )
   A. 选择银行卡图片
   B. 调用云函数识别银行卡号
   C. 上传图片到云存储
   D. 获取图片临时链接

138. 课程中提到，微搭平台可支持的典型能力包括( **ABCD** )
   A. 腾讯会议、腾讯文档等生态打通
   B. 微信支付接入
   C. 企业微信工作流消息推送
   D. 用户权限管理

139. 课程中提到，用户标签的作用包括( **ABCD** )
   A. 作为数据分析基础
   B. 进行市场细分和精准定位
   C. 辅助风险管理和合规识别
   D. 提供个性化服务体验

140. 私域体系搭建过程中，课程中提到的关键动作包括( **ABCD** )
   A. 选择合适的私域渠道
   B. 建立用户社群与会员制度
   C. 持续进行数据分析与优化
   D. 制定内容策略

141. 课程中提到，云存储支持的常见能力包括( **ABCD** )
   A. 下载
   B. 搜索
   C. 删除
   D. 上传

142. 课程中提到，私域运营的价值主要体现在( **ABCD** )
   A. 紧握用户资产并深挖用户价值
   B. 降低营销成本
   C. 提升复购率和忠诚度
   D. 通过数据驱动强化商品或服务管理

143. 相册小程序登录成功后，页面或全局数据中会保存的信息包括( **ABD** )
   A. userInfo
   B. openID
   C. 用户图片列表
   D. 用户头像昵称信息

144. 新闻小程序管理页中，课程实现的功能包括( **ABCD** )
   A. 关键词搜索
   B. 批量删除
   C. 批量更新创建人
   D. 升序/降序切换

145. 新闻新增/编辑页面中，课程要求填写或处理的内容包括( **ABCD** )
   A. 副标题
   B. 新闻内容
   C. 作者
   D. 标题

146. 相册分享小程序的核心功能包括( **ABCD** )
   A. 长按删除图片
   B. 下载图片到本地
   C. 上传图片到云存储
   D. 页面转发分享

147. 课程中提到，常见的私域运营渠道包括( **ABCD** )
   A. 微信群
   B. 微信公众号
   C. 视频号
   D. 微信小程序

148. 课程中私域运营链路涉及的主要环节包括( **ABCD** )
   A. 复购
   B. 留存
   C. 拉新
   D. 转化

149. 关于公域流量与私域流量的区别，课程中提到的维度包括( **ABCD** )
   A. 获取方式
   B. 触达成本
   C. 用户互动性
   D. 所有权

150. 银行卡包项目中，新增银行卡页面包含的主要输入或选择项有( **ABCD** )
   A. 保存按钮
   B. 卡类型
   C. 银行名称
   D. 银行卡号
