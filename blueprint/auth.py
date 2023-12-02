from flask import Blueprint, request, render_template, url_for, redirect, session

from exts import db
from models import UserModel
from .forms import RegisterForm, Loginform

bp = Blueprint('auth', __name__, '/auth')


# 用户登录页
@bp.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = Loginform(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            user = UserModel.query.filter_by(username=username, password=password).first()
            if user:
                session['user_id'] = user.id
                return redirect('/')
            else:
                error = '账号或密码错误'
                return render_template('login.html', error=error)
        error = '账号或密码错误'
        return render_template('login.html', error=error)


# 注册函数
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            username = form.username.data
            password = form.password.data
            email = form.email.data
            new_user = UserModel(username=username, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            # {'email':[邮箱已经被注册]}
            data = '邮箱已经注册或两次密码不一致'
            return render_template('register.html', error=data)


# 注销登录
@bp.route('/')
def logout():
    session.clear()
    return redirect(url_for('/.index'))
