from flask import Flask, request, jsonify
from negocio import agregar_producto_logica, obtener_productos_logica

app = Flask(__name__)

@app.route('/agregar', methods=['POST'])
def agregar_producto():
    data = request.get_json()
    nombre = data.get('nombre')
    resultado = agregar_producto_logica(nombre)
    return jsonify(resultado)

@app.route('/listar', methods=['GET'])
def listar_productos():
    productos = obtener_productos_logica()
    return jsonify({"productos": productos})

if __name__ == '__main__':
    app.run(debug=True)