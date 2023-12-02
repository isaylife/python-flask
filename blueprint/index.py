from flask import Blueprint, render_template

from models import Article, UserModel
import markdown2
bp = Blueprint('/', __name__, '/')


@bp.route('/')
def index():
    data = Article.query.order_by(Article.article_time.desc()).all()
    for article in data:
        user = UserModel.query.get(article.article_author)
        if user:
            article.author_username = user.username  # 将用户名添加到 Article 对象中
            article.avatar = user.avatar
        else:
            article.author_username = "Unknown"  # 或者在用户不存在时设置默认值
    return render_template('index.html', data=data)


@bp.route('/article/<int:post_id>')
def article(post_id):
    data = Article.query.filter_by(id=post_id)
    for article in data:
        user = UserModel.query.get(article.article_author)
        html_content =  markdown2.markdown(article.article_content)
        if user:
            article.username = user.username  # 将用户名添加到 Article 对象中
            article.avatar = user.avatar
        else:
            article.username = "Unknown"  # 或者在用户不存在时设置默认值
    return render_template('acticle.html', articles=data,html_content=html_content)
# 搜索功能
