from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, SelectField, FileField
from wtforms.validators import DataRequired
from flask_wtf.file import FileAllowed

class AquariumForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    type = SelectField('Type', choices=[('Freshwater', 'Freshwater'), ('Brackish', 'Brackish'), ('Saltwater', 'Saltwater')], validators=[DataRequired()])
    image = FileField('Image (JPG, GIF, PNG only)', validators=[FileAllowed(['jpg', 'png', 'gif'], 'JPG, GIF or PNG files only')])
    fish = TextAreaField('Fish', validators=[DataRequired()])
    plants = TextAreaField('Plants', validators=[DataRequired()])
    submit = SubmitField('Post')