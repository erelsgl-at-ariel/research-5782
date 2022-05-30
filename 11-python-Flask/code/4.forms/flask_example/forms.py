from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, InputRequired, NumberRange, URL, Regexp

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=2, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class DataForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    age = IntegerField("Age", validators=[InputRequired(), NumberRange(0,120)])
    homepage = StringField("Homepage", validators=[DataRequired(), Regexp("https?://.*")])
    submit = SubmitField('Compute')

