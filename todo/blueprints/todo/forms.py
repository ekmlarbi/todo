from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class TodoForm(FlaskForm):
    name = StringField('Name', [DataRequired(), Length(3, 255)])