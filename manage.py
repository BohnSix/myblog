from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db
from app.models import *

app = create_app(config_name="develop")


@app.template_filter()
def countTime(content):
    return int(content.__len__() / 200) + 1


manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(db=db, Article=Article, User=User, Category=Category)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)

if __name__ == "__main__":
    # db.drop_all(app=app)
    # db.create_all(app=app)
    app.run(host="0.0.0.0", port=8080, debug=True)
