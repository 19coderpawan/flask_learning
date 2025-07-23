'''✅ Imports the base FlaskForm class from the flask_wtf module.
This is the parent class you’ll inherit from to create any form in Flask-WTF.
It automatically adds CSRF protection and form integration with Flask.'''
from flask_wtf import FlaskForm

''' This imports specific form field types from the WTForms library:
StringField: Used for text input (like name, branch, email, etc.)
SubmitField: Renders a submit button on your form.'''
from wtforms import StringField,SubmitField

'''Imports a built-in validator:
DataRequired(): Ensures the field is not empty when the form is submitted.
If the field is left blank, the form will not validate and will show an error message.'''
from wtforms.validators import DataRequired


class EmployeeForm(FlaskForm): #here EmployeeForm class inherits the FlaskForm class.
    name=StringField('Name',validators=[DataRequired()]) #✅ name is a text input field labeled “Name” It must be filled in, or form submission will fail.validators=[DataRequired()] enforces that rule.
    department=StringField('Department',validators=[DataRequired()])#same like name department is the input field .
    submit=SubmitField('Submit')#here submit is the input field which Triggers form submission
