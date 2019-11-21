from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
    content = CKEditorField(validators=[DataRequired()])
    submit = SubmitField(u'提交')


class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[DataRequired(), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class ArticleForm(FlaskForm):
    title = StringField(u"标题", validators=[DataRequired(), Length(1, 64)])
    summary = TextAreaField(u"简介")
    content = CKEditorField(u"文章", validators=[DataRequired()])
    # source = SelectField(u"来源")
    # type = SelectField(u"类型")
    submit = SubmitField(u"提交")


class RichTextForm(FlaskForm):
    title = StringField(u"标题", validators=[DataRequired(), Length(1, 64)])
    content = CKEditorField(u"文章", validators=[DataRequired()])
    summary = TextAreaField(u"简介")
    submit = SubmitField(u"提交")


class EditArticleForm(FlaskForm):
    title = StringField(u"标题", validators=[DataRequired(), Length(1, 64)])
    summary = CKEditorField(u"简介")
    content = CKEditorField(u"文章", validators=[DataRequired()])
    submit = SubmitField(u"提交")


class EditPostForm(FlaskForm):
    content = TextAreaField(u"内容", validators=[DataRequired()])
    submit = SubmitField(u"提交")


class EditBlogInfoForm(FlaskForm):
    title = StringField(u"博客名", validators=[DataRequired(), Length(1, 64)])
    signature = StringField(u"个性签名", validators=[DataRequired(), Length(1, 64)])
    name = StringField(u"用户名", validators=[DataRequired(), Length(1, 64)])
    selfIntro = StringField(u"自我介绍", validators=[DataRequired(), Length(1, 64)])
    github = StringField(u"github地址", validators=[DataRequired(), Length(1, 64)])
    email = StringField(u"邮箱", validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField(u"提交")
