from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (StringField, SubmitField, TextAreaField, BooleanField)
from wtforms.validators import DataRequired, Length


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=128)])
    content = TextAreaField('Content')
    post_image = FileField('Header image', validators=[
        FileAllowed(['jpg', 'png'], 'Only images are allowed')
    ])
    submit = SubmitField('Save')


class UserAdminForm(FlaskForm):
    is_admin = BooleanField('Administrator')
    submit = SubmitField('Save')
