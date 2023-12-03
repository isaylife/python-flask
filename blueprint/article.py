from flask import Blueprint, render_template, request, redirect, url_for, g
from decorators import login_required
from exts import db
from models import Article,Review_content
import markdown2

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

#发表评论和回复评论
@bp.route('/<int:article_id>',methods=['POST','GET'])
def view_article(article_id):
    if request.form.get('review_content'):
        if request.method == 'POST':
            form = request.form
            review_content = form.get('review_content')
            parent_id = form.get('parent_id')
            parent_id = int(parent_id) if parent_id else None
            new_review = Review_content(
                review_content=review_content,
                article_id=article_id,
                parent_id = parent_id
            )
            db.session.add(new_review)
            db.session.commit()
            return redirect(url_for('article.view_article',article_id=article_id))
    #查询文章
    article = Article.query.get(article_id)
    article_content = markdown2.markdown(article.article_content)
    comments = Review_content.query.filter_by(article_id=article_id,parent_id=None).all()
    return render_template('acticle.html',article=article,comments=comments,article_content=article_content)
# 搜索实现
@bp.route('')
def search():
    # search?=q
    search = request.args.get("search")
    search_all = Article.query.filter(Article.article_title.contains(search)).all()
    return render_template('index.html', data=search_all)
