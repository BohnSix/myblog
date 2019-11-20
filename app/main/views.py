from flask import render_template, request, url_for, current_app, flash, redirect
from flask_login import login_user, current_user

from app.auth.forms import LoginForm
from app.main import main
from app.models import *


@main.route('/')
def index():
    articles = Article.query.order_by(Article.timestamp.desc())
    return render_template('index.html', articles=articles)


@main.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash(u'用户名或密码错误！', 'danger')
    if form.errors:
        flash(u'登陆失败，请尝试重新登陆！', 'danger')
    return render_template('login.html', form=form)


@main.route("/resume/", methods=["GET", "POST"])
def show_resume():
    return render_template("resume.html")


@main.route('/wbsy/')
def wbsy():
    if current_user.is_authenticated:
        return redirect(url_for("auth.wbsy"))
    page = request.args.get('page', 1, type=int)
    categories = Category.query.all()
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.wbsy', page=posts.next_num if posts.has_next else None)
    prev_url = url_for('main.wbsy', page=posts.prev_num if posts.has_prev else None)
    return render_template('wbsy.html', posts=posts.items, categories=categories,
                           next_url=next_url, prev_url=prev_url)


@main.route('/me/', methods=["GET", "POST"])
def about_me():
    return render_template("me.html")
