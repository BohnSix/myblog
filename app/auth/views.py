import os

from flask import url_for, render_template, request, redirect, current_app, jsonify, app, Response
from flask_login import login_required, logout_user

from app.auth import auth
from app.auth.forms import PostForm, ArticleForm, EditArticleForm, EditPostForm
from app.models import *

from datetime import datetime


@auth.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@auth.route('/wbsy/', methods=["GET", "POST"])
@login_required
def wbsy():
    form = PostForm()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.wbsy', page=posts.next_num if posts.has_next else None)
    prev_url = url_for('main.wbsy', page=posts.prev_num if posts.has_prev else None)

    if form.validate_on_submit():
        post = Post(content=form.content.data, timestamp=datetime.now())
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('auth.wbsy', form=form, posts=posts.items,
                                next_url=next_url, prev_url=prev_url))
    return render_template('wbsy.html', form=form, posts=posts.items,
                           next_url=next_url, prev_url=prev_url)


@auth.route("/resume/", methods=["GET", "POST"])
def show_resume():
    cs = Category.query.all()
    return redirect(url_for("main.show_resume", categories=cs))


@auth.route("/writing_article/", methods=["GET", "POST"])
@login_required
def writing_article():
    form = ArticleForm()
    if form.validate_on_submit():
        a = Article(title=form.title.data,
                    content=form.title.data,
                    summary=form.summary.data)
        db.session.add(a)
        db.session.commit()
        return redirect(url_for('auth.index'))
    return render_template('auth/writing.html', form=form)


@auth.route("/management/")
@login_required
def manage():
    articles = Article.query.order_by(Article.timestamp.desc())
    posts = Post.query.order_by(Post.timestamp.desc())

    return render_template('auth/management.html', articles=articles, posts=posts)


@auth.route("/management/article/<int:id>", methods=["GET", "POST"])
@login_required
def edit_article(id):
    article = Article.query.filter_by(id=id).first()
    form = EditArticleForm()

    if form.validate_on_submit():
        article.title=form.title.data
        article.summary=form.summary.data
        article.content=form.content.data

        db.session.commit()
        return redirect(url_for('auth.manage'))
    form.title.data = article.title
    form.summary.data = article.summary
    form.content.data = article.content
    return render_template('auth/edit.html', form=form)



@auth.route("/management/del_article/<int:id>")
@login_required
def del_article(id):
    article = Article.query.filter_by(id=id).first()
    if article is not None:
        db.session.delete(article)
        db.session.commit()
    return redirect(url_for('auth.manage'))



@auth.route("/management/post/<int:id>", methods=["GET", "POST"])
@login_required
def edit_post(id):
    post = Post.query.filter_by(id=id).first()

    form = EditPostForm()

    if form.validate_on_submit():
        post.content=form.content.data
        post.timestamp=datetime.now()
        db.session.commit()
        return redirect(url_for('auth.manage'))

    form.content.data = post.content
    return render_template('auth/edit.html', form=form)



@auth.route("/management/del_post/<int:id>")
@login_required
def del_post(id):
    post = Post.query.filter_by(id=id).first()
    if post is not None:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('auth.manage'))


# 图片上传处理
@auth.route('/upload/',methods=['POST'])
def upload():
    file=request.files.get('editormd-image-file')
    if not file:
        res={
            'success':0,
            'message':u'图片格式异常'
        }
    else:
        ex=os.path.splitext(file.filename)[1]
        filename=datetime.now().strftime('%Y%m%d%H%M%S')+ex
        from app import app
        file.save(os.path.join(app.config['SAVEPIC'],filename))
        #返回
        res={
            'success':1,
            'message':u'图片上传成功',
            'url':url_for('.image',name=filename)
        }
    return jsonify(res)

#编辑器上传图片处理
@auth.route('/image/<name>')
def image(name):
    with open(os.path.join(app.config['SAVEPIC'],name),'rb') as f:
        resp=Response(f.read(),mimetype="image/jpeg")
    return resp
