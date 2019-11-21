from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager


@login_manager.user_loader
def loader_user(user_id):
    return User.query.filter_by(id=user_id).first()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        return AttributeError("Password is not a readable attribute!")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.username


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(32), index=True, unique=True)
    articles = db.relationship('Article', backref="categories", lazy="dynamic")

    def delete_category(self, name):
        pass

    def __repr__(self):
        return '<Category %r>' % self.name


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    content = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)

    def __repr__(self):
        return self.content


class Article(db.Model):
    __tablename__ = 'articles'
    id = db.Column(db.Integer, unique=True, primary_key=True, autoincrement=True)
    title = db.Column(db.String(64), index=True)
    content = db.Column(db.Text)
    summary = db.Column(db.Text)
    num_of_view = db.Column(db.Integer, default=0)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)
    length = db.Column(db.Integer, default=0)
    category = db.Column(db.String(32), db.ForeignKey("categories.name"))

    @staticmethod
    def add_view(article, db):
        article.num_of_view += 1
        db.session.add(article)
        db.session.commit()

    def __repr__(self):
        return '<Article %r>' % self.title


class BlogInfo(db.Model):
    __tablename__ = 'blogInfo'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    signature = db.Column(db.Text)
    name = db.Column(db.String(64))
    selfIntro = db.Column(db.Text)
    github = db.Column(db.String(64))
    email = db.Column(db.String(64))
    # friendLink = db.Column(db.String(64))  # 用外键连接一张表
    # avatar = db.Column(db.Text)


# class BlogView(db.Model):
#     __tablename__ = 'blogView'
#     id = db.Column(db.Integer, primary_key=True)
#     num_of_view = db.Column(db.BigInteger, default=0)
#
#     @staticmethod
#     def insert_view():
#         view = BlogView(num_of_view=0)
#         db.session.add(view)
#         db.session.commit()
#
#     @staticmethod
#     def add_view():
#         view = BlogView.query.first()
#         view.num_of_view += 1
#         db.session.add(view)
#         db.session.commit()
