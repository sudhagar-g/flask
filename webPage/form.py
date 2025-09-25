from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from webPage.module import User



class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2, max=20)])
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirm = PasswordField('Confirm password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('sign up')


    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken.please choose a another name')


class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')    


    def validate_email(self,email):
        user = User.query.filter_by(username=email.data).first()
        if user:
            raise ValidationError('That email is taken.please choose a differt one')



