# 用户信息面板

import os

from flask import Blueprint, g, render_template, request, redirect, url_for

from decorators import login_required
from exts import db
from models import UserModel
from .forms import Update_info

bp = Blueprint('board', __name__)


# 用户信息
@bp.route('/board/info')
@login_required
def user_info():
    user_info = UserModel.query.filter_by(id=g.user.id).all()
    return render_template('board.html', data=user_info)


# 修改用户名
@bp.route('/board/update', methods=['POST','GET'])
@login_required
def user_info_update():
    form = Update_info(request.form)
    if form.validate():
        user_chage_name = form.username.data
        UserModel.query.filter_by(id=g.user.id).update({'username': user_chage_name})
        db.session.commit()
        return redirect(url_for('board.user_info'))
    return redirect(url_for('board.user_info'))


# 上传头像
@bp.route('/board/avatar', methods=['POST'])
def upload_avatar():
    file_path = os.path.abspath('static/images/')
    file = request.files.get('file')
    filename = file.filename.split('.')[-1]
    suppot = ['jpg', 'png', 'jpeg']
    if filename in suppot:
        file_size = request.content_length / 1024
        if file_size > 1000:
            return url_for('board.user_info')
        file_name = f'{g.user.username}.' + filename
        file_upload = os.path.join(file_path, file_name)
        print(g.user.id)
        UserModel.query.filter_by(id=g.user.id).update({'avatar': file_name})
        db.session.commit()
        file.save(file_upload)
    return redirect(url_for('board.user_info'))
