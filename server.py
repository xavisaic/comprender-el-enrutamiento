from flask import Flask

app = Flask(__name__)

@app.route('/saludar')
def saludar():
    return 'HOLA MUNDO'


@app.route('/dojo')
def dojo():
    return 'Dojo'

@app.route('/say/<nombre>')
def decir(nombre):
    return f'hola,{nombre}!!!!'

@app.route('/repeat/<int:num>/<string:word>')
def repetir(num, word):
    texto = (word +' ')*num
    return str(texto)

@app.errorhandler(404)
def error(e):
    return '<h3> Lo siento, no hay respuesta, intentalo otra vez </h3>'



if __name__ == '__main__':
    app.run(debug = True)

