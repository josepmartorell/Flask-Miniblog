from flask_wtf import FlaskForm, Form, CSRFProtect
from wtforms import SubmitField, TextAreaField, StringField
from wtforms.validators import DataRequired

csrf = CSRFProtect()


class CommentForm(FlaskForm):
    content = TextAreaField('Content', validators=[DataRequired(), ])
    submit = SubmitField('Comment')


class ContactForm(Form):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")
