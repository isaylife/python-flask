document.addEventListener('DOMContentLoaded', function () {
  // 在文本框上初始化 SimpleMDE，并指定语言
  var simplemde = new SimpleMDE({
    element: document.getElementById("blogEditor"),
    spellChecker: false, // 可选的配置选项
    language: 'zh-CN'  // 设置为中文
  });
});