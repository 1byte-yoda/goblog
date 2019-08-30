from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms import ValidationError
from wtforms.validators import DataRequired, Email, Length, EqualTo, Regexp
from .. models import User

class LoginForm(FlaskForm):
    email = StringField('Email ', validators=[DataRequired(), 
                        Email(), Length(1, 60)])
    password = PasswordField('Password ', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    email_validators = [DataRequired(), Email(),
                        Length(1, 68)]
    password_validators = [DataRequired(), 
                           EqualTo('password2', 'Password must match!')]
    username_validators = [DataRequired(),
                           Length(1, 68),
                           Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                  'Username must only contain letters, \
                                  numbers, underscores and dots')]

    email = StringField('Email ', validators=email_validators)
    username = StringField('Username ', validators=username_validators)
    password = PasswordField('Password ', validators=password_validators)
    password2 = PasswordField('Confirm Password ', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already taken!')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already taken!')
