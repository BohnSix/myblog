import random

from faker import Faker
from sqlalchemy.exc import InterfaceError

from app.models import *
from app import db

f = Faker("zh_CN")


def forge_admin():
    user = User(username="Bohnsix", email="bohnsix@163.com")
    user.password = "123"
    db.session.add(user)
    db.session.commit()


def forge_blogInfo():
    blogInfo = BlogInfo(title="Bohn's pit",
                        name=u'bohnsix',
                        signature=u"高度自律即绝对自由",
                        selfIntro=u'flask新手',
                        github=u"https://github.com/bohnsix",
                        email=u'bohnsix@163.com',
                        choose=True)
    db.session.add(blogInfo)
    db.session.commit()


def forge_posts(count=10):
    for i in range(count):
        post = Post(content=f.text(max_nb_chars=200), timestamp=f.date_time_this_year())
        db.session.add(post)
    db.session.commit()


def forge_categories(count=10):
    for i in range(count):
        category = Category(name=f.word())
        db.session.add(category)
        try:
            db.session.commit()
        except InterfaceError:
            db.session.rollback()


def forge_articles(count=10):
    categories = Category.query.all()
    for i in range(count):
        article = Article(title=f.sentence(),
                          summary=f.text(),
                          content=f.text(),
                          category=categories[random.randint(0, Category.query.count() - 1)].name)
        article.length = len(article.content)
        db.session.add(article)
    db.session.commit()
