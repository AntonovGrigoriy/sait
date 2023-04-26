from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, EmailField, IntegerField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    email = EmailField('Логин / почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    age = IntegerField('Возраст', validators=[DataRequired()])
    position = StringField('Профессия', validators=[DataRequired()])
    speciality = StringField('Специальность', validators=[DataRequired()])
    address = StringField('Адрес', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться')


class LoginForm(FlaskForm):
    email = EmailField('Логин / почта', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить')
    submit = SubmitField('Войти')
