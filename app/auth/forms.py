from flask_wtf import FlaskForm
from wtforms import ValidationError, StringField, PasswordField, SubmitField, BooleanField
from ..models import User

class LoginForm(FlaskForm):
    