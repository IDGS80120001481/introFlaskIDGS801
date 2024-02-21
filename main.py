from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
import forms
from wtforms import validators
from flask import flash
from flask import g




app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

app.secret_key = "Esta madre se puso buena"

@app.before_request
def before():
    g.nombre = 'Mario' 
    print('before 1')

@app.after_request
def after(response):
    print('after 3')
    return response

@app.route("/")
def index():
    return render_template("layout3.html")

@app.route("/alumnos", methods=['GET','POST'])
def alumnos():
    print("alumno {}".format(g.nombre))
    nom = ''
    apa = ''
    ama = ''
    edad = ''

    alumno_clase = forms.UserForm(request.form)
    if request.method == 'POST':
        nom = alumno_clase.nombre.data 
        apa = alumno_clase.apaterno.data 
        ama = alumno_clase.amaterno.data 
        edad = alumno_clase.edad.data 
        print('Nombre: {}'.format(nom))
        print('Apaterno: {}'.format(apa))
        print('Amaterno: {}'.format(ama))

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("alumnos2.html", form=alumno_clase, nom = nom, apa = apa, ama = ama)

@app.route("/maestros")
def maestros():
    return render_template("maestros.html")

'''@app.route("/")
def index():
    return "Hola Mundo ¡¡¡¡¡"'''

@app.route("/hola")
def hola():
    return "<h1> Saludos desde el Hola</h1> "

@app.route("/Saludo")
def saludo():
    return "<h1> Saludos desde Saludo</h1> "

@app.route("/nombre/<string:nom>")
def saludo_nombre(nom):
    return "Hola " + nom

@app.route("/numero/<int:n1>")
def mostrar_numero(n1):
    return "Numero: {}".format(n1)

@app.route("/user/<int:id>/<string:nom>")
def user(id,nom):
    return "ID: {} Nombre: {}".format(id,nom)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return "La suma {} + {} = {}".format(n1,n2,n1 + n2)

@app.route("/calcular" , methods=["GET", "POST"])
def calcular():
    if request.method== "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1) * int(num2))) 
    else:
        return '''
        <form action="/calcular" method="POST">
            <label>N1:</label>
            <input type="text" name="n1"><br>
            <label>N2:</label>
            <input type="text" name="n2"><br>
            <input type="submit">
        </form>
    '''

@app.route("/OperasBas" , methods=["GET", "POST"])
def operasbas():
    return render_template("OperasBas.html")

@app.route("/resultado")
def result():
    if request.method== "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        return "La multiplicacion de {} x {} = {}".format(num1,num2,str(int(num1) * int(num2))) 
    else:
        return render_template("OperasBas.html")

    

@app.route("/default")
@app.route("/default/<string:d>")
def func3(d="Dario"):
    return "El nombre del usuario es: " + d




if __name__ == "__main__":
    app.run(debug=True)