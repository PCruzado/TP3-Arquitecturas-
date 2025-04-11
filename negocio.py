from datos import agregar_producto_db, obtener_productos_db

def agregar_producto_logica(nombre):
    if not nombre:
        return {"error": "El nombre del producto es obligatorio."}
    agregar_producto_db(nombre)
    return {"mensaje": f"Producto '{nombre}' agregado con éxito."}

def obtener_productos_logica():
    return obtener_productos_db()