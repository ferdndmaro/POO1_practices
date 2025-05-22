#Uso de FLask
#Oscar Fernando Madera Rojo 2B

from flask import Flask 
app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return 'holaaaaa'

if __name__ == '__main__':
    app.run(debug = True)


