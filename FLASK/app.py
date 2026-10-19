
# week = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]
# # weekT = ("Lunes")

# # for i,day in enumerate(week):
# #     print(f"{i} {day}")


# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def inicio():
#         return '<h1>Hola Mundo con Flask<h1>'



# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint HTML
@app.route('/')
def inicio():
    return """
    <html>
        <body>
            <h1>Hola Mundo</h1>
            <a href="http://127.0.0.1:5000/api/saludo">Buscar Datos</>
        </body>
    </html>
    """

# Endpoint JSON
@app.route('/api/saludo')
def saludo():
    return jsonify({
        "mensaje": "Hola Mundo",
        "estatus": "ok"
    })

if __name__ == '__main__':
    app.run(debug=True)