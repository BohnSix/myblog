import click
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor

from config import config

db = SQLAlchemy()
moment = Moment()
bootstrap = Bootstrap()
migrate = Migrate(db=db)
login_manager = LoginManager()
ckeditor = CKEditor()
# login_manager.session_protection = 'strong'
login_manager.login_view = "auth.login"


def register_commands(app):
    @app.cli.command()
    @click.option("--drop", is_flag=True, help="Create after drop")
    def init_db(drop):
        if drop:
            click.comfirm("This operation will delete your database, do you want to continue?", abort=True)
            db.drop_all()
            click.echo("Table droped")
        db.create_all()
        click.echo("Initialized database")

    @app.cli.command()
    @click.option("--categories", default=10, help="Quantity of categories, default is 10")
    @click.option("--posts", default=20, help="Quantity of posts, default is 10")
    @click.option("--articles", default=10, help="Quantity of articles, default is 10")
    def forge(categories, posts, articles):
        from app.forge import forge_admin, forge_posts, forge_blog, forge_articles, forge_categories

        click.echo("Generating admin...")
        # forge_admin()

        click.echo("Generating %d categories..." % categories)
        forge_categories(categories)

        click.echo("Generating %d posts..." % posts)
        forge_posts(posts)

        click.echo("Generating %d articles..." % articles)
        forge_articles(articles)

        click.echo("Done")


def create_app(config_name="default"):
    app = Flask(__name__)

    app.config.from_object(config[config_name])

    db.init_app(app)
    moment.init_app(app)
    bootstrap.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)
    ckeditor.init_app(app)

    register_commands(app)

    from app.main import main
    app.register_blueprint(main)

    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app
