from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista en memoria para almacenar productos
productos = []

# Ruta para agregar productos
@app.route('/agregar', methods=['POST'])
def agregar_producto():
    data = request.get_json()
    nombre = data.get('nombre')
    if nombre:
        productos.append(nombre)
        return jsonify({"mensaje": f"Producto '{nombre}' agregado con éxito."})
    else:
        return jsonify({"error": "Falta el nombre del producto."}), 400

# Ruta para listar productos
@app.route('/listar', methods=['GET'])
def listar_productos():
    return jsonify({"productos": productos})

if __name__ == '__main__':
    app.run(debug=True)

# --------------------- Explicación ---------------------
# Esta implementación es monolítica porque toda la aplicación
# (presentación, lógica de negocio y almacenamiento) está contenida
# en un solo archivo. No hay separación en módulos ni capas.
# 
# Desventajas:
# - Difícil de escalar: al crecer la app, el código se vuelve difícil de mantener.
# - Bajo nivel de reutilización: todo está acoplado.
# - Limitado para trabajar en equipo: varias personas modificando el mismo archivo puede generar errores.