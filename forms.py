from wtforms import Form
from wtforms import StringField, TelField, IntegerField

from wtforms import EmailField
from wtforms.validators import DataRequired, Email


class UserForm(Form):
    nombre = StringField('nombre')
    email = StringField("email")
    apaterno = TelField("apaterno")
    amaterno = StringField('amaterno')
    edad = IntegerField('edad')