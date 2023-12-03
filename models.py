from datetime import datetime

from exts import db


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    avatar = db.Column(db.String(30))


class Article(db.Model):
    __tablename__ = "article"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    article_title = db.Column(db.String(200), nullable=False)
    article_content = db.Column(db.Text, nullable=False)
    article_time = db.Column(db.DateTime, default=datetime.now())
    # 外键
    article_author = db.Column(db.Integer, db.ForeignKey("user.id"))
    # 返回该作者的所以文章
    authorall = db.relationship(UserModel, backref="article")

class Review_content(db.Model):
    __tablename__ = "review"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    review_content = db.Column(db.Text, nullable=False)
    review_time = db.Column(db.DateTime,default=datetime.now())

    #添加外键
    article_id = db.Column(db.Integer,db.ForeignKey('article.id'))
    # 反向查询
    #使用article.comments可以查询文章评论
    article = db.relationship('Article',backref='comments')

    #添加父评论字段
    parent_id = db.Column(db.Integer,db.ForeignKey('review.id'))#添加外键链接评论id
    parent = db.relationship('Review_content',remote_side=[id],backref='replies')

