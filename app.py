# 学习python开发的论坛系统
# 后端就用flask
# 数据库使用orm模型
# 分别实现什么功能
# 1、登录注册
#     实现登录
#     实现注册
#     邮件发送验证码
# 2、蓝图模块
#     主页
#     登录
#     注册
#     内容信息页
#     控制面板页
#
from datetime import timedelta
from flask import Flask, session, g
from flask_migrate import Migrate

import config
from blueprint.article import bp as article
from blueprint.auth import bp as auth
from blueprint.board import bp as user_board
from blueprint.index import bp as index
from exts import db



from models import UserModel

app = Flask(__name__)
# 导入config
app.config.from_object(config)
# 设置session过期时间120分钟
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=120)
# 使用markdown渲染
db.init_app(app)
migrate = Migrate(app, db)

# 蓝图注册
app.register_blueprint(user_board, url_prefix='/auth')
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(index)
app.register_blueprint(article, url_prefix='/article')


@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = UserModel.query.get(user_id)
        if user:
            setattr(g, "user", user)
    else:
        setattr(g, "user", None)


# 上下文处理器
@app.context_processor
def my_context_processor():
    # print(f"上下文处理器的{g.user}")
    return {"user": g.user}


# #钩子函数 before_request
# @app.before_request
# def my_before_request():
#     user_id = session.get('user_id')
#     if user_id:
#         user = UserModel.query.get(user_id)
#         setattr(g,'user',user)
#     else:
#         setattr(g,'user',None)
#
# #上下文处理器
# @app.context_processor
# def my_context_processor():
#     return {'user':g.user}

if __name__ == '__main__':
    app.run(debug=True)
