from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms import BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job = StringField('Название блюда', validators=[DataRequired()])
    work_size = IntegerField('Время готовки', validators=[DataRequired()])
    collaborators = StringField('Список ингридиентов')
    is_finished = BooleanField('Полезно ли')
    submit = SubmitField('Сохранить')