from flask_wtf import FlaskForm
from wtforms import TextAreaField, StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, Length
from flask_ckeditor import CKEditorField


class PostForm(FlaskForm):
    content = TextAreaField(validators=[DataRequired()])
    submit = SubmitField(u'提交')


class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[DataRequired(), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    submit = SubmitField(u'提交')


class ArticleForm(FlaskForm):
    title = StringField(u"标题", validators=[DataRequired(), Length(1, 64)])
    content = TextAreaField(u"文章", validators=[DataRequired()])
    summary = TextAreaField(u"简介")
    # source = SelectField(u"来源")
    # type = SelectField(u"类型")
    submit = SubmitField()


class RichTextForm(FlaskForm):
    title = StringField(u"标题", validators=[DataRequired(), Length(1, 64)])
    content = CKEditorField(u"文章", validators=[DataRequired()])
    summary = TextAreaField(u"简介")
    submit = SubmitField(u"提交")

class EditArticleForm(FlaskForm):
    title = StringField(u"标题", validators=[DataRequired(), Length(1, 64)])
    content = TextAreaField(u"文章", validators=[DataRequired()])
    summary = TextAreaField(u"简介")
    submit = SubmitField(u"提交")


class EditPostForm(FlaskForm):
    content = TextAreaField(u"内容", validators=[DataRequired()])
    submit = SubmitField(u"提交")
