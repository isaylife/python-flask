document.addEventListener('DOMContentLoaded', function () {
  // 在文本框上初始化 SimpleMDE，并指定语言
  var simplemde = new SimpleMDE({
    element: document.getElementById("blogEditor"),
    spellChecker: false, // 可选的配置选项
  });
});
// script.js

document.querySelectorAll('.reply-btn').forEach(button => {
    button.addEventListener('click', function (event) {
        event.preventDefault();
        // 获取 data-target 属性值，即评论的 ID
        const targetCommentId = this.getAttribute('data-target');
        // 设置目标评论的 ID 到隐藏字段
        document.getElementById('parent_id').value = targetCommentId;
        // 设置回复表单的占位符为 '回复'，并将已有的值插入到占位符中
        document.getElementById('new_comment_form').querySelector('input[name="review_content"]').placeholder = '回复';

        window.location.hash = 'new_comment_form';
    });
});
// 验证评论内容是否为空
function validateAndSubmit() {
    var reviewContent = document.getElementById('review_content').value;

    // 检查是否为空
    if (reviewContent.trim() === '') {
        document.getElementById('review_content_error').innerText = '评论内容不能为空';
        return;
    }

    // 如果输入不为空，清空错误信息并提交表单
    document.getElementById('review_content_error').innerText = '';
    document.getElementById('new_comment_form').submit();
}
function LoginvalidateForm() {
    // 获取用户名和密码输入框的值
    var username = document.getElementById('username').value;
    var password = document.getElementById('exampleInputPassword1').value;

    // 检查是否为空
    if (username.trim() === '' || password.trim() === '') {
        alert('用户名和密码不能为空');
        return false; // 阻止表单提交
    }

    // 如果输入不为空，可以继续处理表单提交等逻辑
    return true;
}
function RegistervalidateForm(){
    var email = document.getElementById('InputEmail').value;
    var username = document.getElementById('InputUsername').value;
    var password = document.getElementById('InputPassword').value;
    var password2 = document.getElementById('password_confirm').value;
    if (email.trim() === '' || username.trim() ===''|| password.trim()==='' || password2.trim()===''){
        alert('请检查输入是否有误');
        return false
    }
    return true
}