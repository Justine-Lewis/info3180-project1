import flask_wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange


#PropertyForm class, Accepts only jpg,jpeg,png files to be uploaded
#Accepts all fields for property creation
class PropertyForm(FlaskForm):
    title = StringField('Property Title', validators=[DataRequired()])
    bedrooms = IntegerField('No. of Bedrooms', validators=[DataRequired()])
    bathrooms = IntegerField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    property_type = SelectField(
        'Property Type',
        choices=[('House', 'House'), ('Apartment', 'Apartment')],
        validators=[DataRequired()]
    )
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField(
        'Photo',
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], 'Browse For Photos!')
        ]
    )
    submit = SubmitField('Add Property')
    