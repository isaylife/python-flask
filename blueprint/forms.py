# 表单验证类
import wtforms
from wtforms.validators import Length, Email, EqualTo

from models import UserModel


class RegisterForm(wtforms.Form):
    email = wtforms.StringField(Email(message='邮箱格式错误'))
    password = wtforms.StringField(validators=[Length(min=6, max=200, message='密码格式错误')])
    password_confirm = wtforms.StringField(validators=[EqualTo('password', message='两次密码不一样')])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message='用户名格式错误')])

    # 验证数据库是否存在该邮箱
    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message='该邮箱已经被注册')

    # 验证数据库是否存在改用户名
    def validate_username(self, field):
        username = field.data
        user = UserModel.query.filter_by(username=username).first()
        if user:
            raise wtforms.ValidationError(message='该用户名已经被使用')


class Loginform(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=3, max=12, message='用户名错误')])
    password = wtforms.StringField(validators=[Length(min=3, max=12, message="密码错误")])


# 更新验证
class Update_info(wtforms.Form):
    username = wtforms.StringField(validators=[Length(min=3, max=12, message='请重新输入信息')])

    def validate_username(self, field):
        username = field.data
        user = UserModel.query.filter_by(username=username).first()
        if user:
            raise wtforms.ValidationError(message='该用户名已经存在')
