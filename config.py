import os
import sys

base_dir = os.path.abspath(os.path.dirname(__file__))

WIN = sys.platform.startswith('win')
if WIN:
    pre = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class Config:
    SECRET_KEY = 'f461c14a47d0409dac0bc5cb70af4ab7'

    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or \
                              pre + os.path.join(base_dir, 'data.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE = 15
    ARTICLES_PER_PAGE = 15
    CKEDITOR_SERVE_LOCAL = True

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = pre + os.path.join(base_dir, 'DevData.sqlite')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class ProductConfig(Config):
    pass


config = {
    'develop': DevelopmentConfig,
    'testing': TestingConfig,
    'product': ProductConfig,
    'default': DevelopmentConfig
}
