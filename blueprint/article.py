from flask import Blueprint, render_template, request, redirect, url_for, g
from decorators import login_required
from exts import db
from models import Article

bp = Blueprint('article', __name__)


# 文章发布
@bp.route('/add', methods=['POST', 'GET'])
@login_required
def article_add():
    if request.method == 'GET':
        return render_template('acticle_add.html')
    else:
        form = request.form
        article_title = form.get('article_title')
        article_content = form.get('article_content')
        article_new = Article(article_title=article_title, article_content=article_content, article_author=g.user.id)
        db.session.add(article_new)
        db.session.commit()
        return redirect(url_for('article.article_add'))


# 删除帖子
@bp.route('/delete/<int:delete_id>')
@login_required
def article_delete(delete_id):
    delete_articel = Article.query.get(delete_id)
    db.session.delete(delete_articel)
    db.session.commit()
    return redirect(url_for("article.article_page"))


# 修改文章
@bp.route('/update/<int:update_id>', methods=['POST', 'GET'])
def article_update(update_id):
    if request.method == 'GET':
        data = Article.query.filter_by(id=update_id)
        return render_template('acticle_update.html', articles=data)
    else:
        form = request.form
        update_title = form['article_title']
        update_content = form['article_content']
        Article.query.filter_by(id=update_id).update({'article_title': update_title, 'article_content': update_content})
        db.session.commit()
        return redirect(url_for('article.article_page'))


# 进入后台管理文章
@bp.route('/manage')
@login_required
def article_page():
    all_article = Article.query.filter_by(article_author=g.user.id).all()
    return render_template('acticle_page.html', data=all_article)


# 文章详情页
@bp.route('/<int:post_id>')
def article(post_id):
    data = Article.query.filter_by(id=post_id)
    return render_template('index.html',articles=data)


# 搜索实现
@bp.route('')
def search():
    # search?=q
    search = request.args.get("search")
    search_all = Article.query.filter(Article.article_title.contains(search)).all()
    return render_template('index.html', data=search_all)
