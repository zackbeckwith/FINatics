from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class AquariumForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    type = TextAreaField('Text', validators=[DataRequired()])
    fish = TextAreaField('Text', validators=[DataRequired()])
    plants = TextAreaField('Text', validators=[DataRequired()])
    submit = SubmitField('Post')