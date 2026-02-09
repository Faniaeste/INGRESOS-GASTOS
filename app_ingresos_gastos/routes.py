from app_ingresos_gastos import app
from flask import render_template,request,redirect
import csv

@app.route("/")
def index():
    datos = []
    fichero = open('app_ingresos_gastos/data/movimientos.csv','r')
    lectura = csv.reader(fichero,delimiter=",",quotechar='"')
    for item in lectura:
        datos.append(item)

    fichero.close()

    """
        datos=[
        {'Fecha':'01/09/2026','concepto':'Salario','monto':1800},
        {'Fecha':'01/09/2026','concepto':'Salario','monto':1800},
        {'Fecha':'01/09/2026','concepto':'Salario','monto':1800},
    ]
    """
    return render_template("index.html", title = "Lista", lista= datos)

@app.route("/new",methods=["GET","POST"])
def new():
    if request.method == "POST":
        #acceder al arcivo y configurar la carga del nuevo registro
        mifichero = open('app_ingresos_gastos/data/movimientos.csv','a',newline="")
        #llamar al metodo writer de escritura y configuramos el formato
        lectura = csv.writer(mifichero,delimiter=",",quotechar='"')
        #registramos los datos recibidos desde el formulario al archivo csv
        lectura.writerow( [request.form['dfecha'],request.form['dconcepto'],request.form['dmonto']] )


        return redirect("/")#esto es para redirigir a la ruta home.
    else:#Esto sería el GET
        return render_template("new.html", title = "Registro", titulo ="Registro", boton="Guardar")

@app.route("/delete")
def delete():
    return render_template("delete.html", title = "Borrar")

@app.route("/update")
def update():
    return render_template("update.html", title = "Actualizar",titulo = "Actualización", boton = "Actualizar")

