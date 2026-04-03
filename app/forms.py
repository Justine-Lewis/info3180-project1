import flask_wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import StringField, TextAreaField, SelectField, SubmitField, IntegerField
from wtforms.validators import DataRequired, InputRequired, NumberRange


#PropertyForm class, Accepts only jpg,jpeg,png files to be uploaded
#Accepts all fields for property creation
class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bedrooms = IntegerField('Bedrooms', validators=[DataRequired()])
    bathrooms = IntegerField('Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    property_type = SelectField(
        'Type',
        choices=[('House', 'House'), ('Apartment', 'Apartment')],
        validators=[DataRequired()]
    )
    description = TextAreaField('Description', validators=[DataRequired()])
    photo = FileField(
        'Photo',
        validators=[
            FileRequired(),
            FileAllowed(['jpg', 'jpeg', 'png'], 'Images only!')
        ]
    )
    submit = SubmitField('Add Property')
    