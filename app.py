from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():

    nombre = "Elio Nicolas"

    apellidos = {
        "primero": "Beltre",
        "segundo": "Alcantara"
    }

    asignaturas = [
        "Programación",
        "Base de Datos",
        "Innovación Empresarial"
    ]

    hobbies = [
        "Jugar videojuegos",
        "Desarrollar páginas web",
        "Escuchar música"
    ]

    return render_template(
        "index.html",
        nombre=nombre,
        apellidos=apellidos,
        asignaturas=asignaturas,
        hobbies=hobbies
    )


if __name__ == "__main__":
    app.run(debug=True)