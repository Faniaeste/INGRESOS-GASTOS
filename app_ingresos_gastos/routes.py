from app_ingresos_gastos import app
from flask import render_template
import csv

@app.route("/")
def index():
    datos = []
    fichero = open('app_ingresos_gastos/data/movimientos.csv','r')
    lectura = csv.reader(fichero,delimiter=",",quotechar='"')
    for item in lectura:
        datos.append(item)

    """
        datos=[
        {'Fecha':'01/09/2026','concepto':'Salario','monto':1800},
        {'Fecha':'01/09/2026','concepto':'Salario','monto':1800},
        {'Fecha':'01/09/2026','concepto':'Salario','monto':1800},
    ]
    """
    return render_template("index.html", title = "Lista")

@app.route("/new")
def new():
    return render_template("new.html", title = "Registro", titulo ="Registro", boton="Guardar")

@app.route("/delete")
def delete():
    return render_template("delete.html", title = "Borrar")

@app.route("/update")
def update():
    return render_template("update.html", title = "Actualizar",titulo = "Actualización", boton = "Actualizar")

