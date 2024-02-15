from wtforms import Form
from wtforms import StringField, TelField, IntegerField

from wtforms import validators
from wtforms.validators import DataRequired, Email



class UserForm(Form):
    nombre = StringField('nombre', [
    validators.DataRequired(message="El campo es requerido"),
    validators.Length(min=4, max=10, message="Ingresa un nombre válido")
    ])
    email = StringField("email", [
    validators.DataRequired(message="El campo es requerido"),
    validators.Length(min=4, max=10, message="Ingresa un nombre válido")
    ])
    apaterno = TelField("apaterno",[
    validators.DataRequired(message="El campo es requerido"),
    validators.Length(min=4, max=10, message="Ingresa un nombre válido")
    ])
    amaterno = StringField('amaterno', [
    validators.DataRequired(message="El campo es requerido"),
    validators.Length(min=4, max=10, message="Ingresa un nombre válido")
    ])
    edad = IntegerField('edad', [
    validators.Email(message='Ingrese una edad válida')])