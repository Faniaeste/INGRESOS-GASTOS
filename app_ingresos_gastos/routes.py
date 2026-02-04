from app_ingresos_gastos import app
from flask import render_template

@app.route("/")
def index():
    datos = [
        {'Fecha':'01/09/2026':'concepto':'Salario','monto':1800},
        {'Fecha':'01/09/2026':'concepto':'Salario','monto':1800},
        {'Fecha':'01/09/2026':'concepto':'Salario','monto':1800},
    ]
    return render_template("index.html", title = "Lista")

@app.route("/new")
def new():
    return render_template("new.html", title = "Registro")

@app.route("/delete")
def delete():
    return render_template("delete.html")

@app.route("/update")
def update():
    return render_template("update.html")

