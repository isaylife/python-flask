from flask import Blueprint,session,render_template,g,request
from models import Article,UserModel
bp = Blueprint('/',__name__,'/')

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
    return render_template('index.html',data=data)
@bp.route('/article/<int:post_id>')
def article(post_id):
    data = Article.query.filter_by(id=post_id)
    for article in data:
        user = UserModel.query.get(article.article_author)
        if user:
            article.username = user.username  # 将用户名添加到 Article 对象中
            article.avatar = user.avatar
        else:
            article.username = "Unknown"  # 或者在用户不存在时设置默认值
    return render_template('acticle.html',articles=data)
#搜索功能
