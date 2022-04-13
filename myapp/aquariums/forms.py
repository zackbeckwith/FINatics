from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired

class AquariumForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    type = SelectField('Type', choices=[('Freshwater', 'Freshwater'), ('Saltwater', 'Saltwater')], validators=[DataRequired()])
    fish = TextAreaField('Fish', validators=[DataRequired()])
    plants = TextAreaField('Plants', validators=[DataRequired()])
    submit = SubmitField('Post')