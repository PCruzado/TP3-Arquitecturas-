# Arquitectura de 3 Capas - App de Productos

## Descripción

Esta aplicación está desarrollada en base a la arquitectura de 3 capas, separando responsabilidades claramente en tres archivos:

### Capas

- **Capa de Presentación (`main.py`)**: Define las rutas HTTP y recibe peticiones del usuario.
- **Capa de Negocio (`negocio.py`)**: Contiene la lógica que valida y procesa los datos.
- **Capa de Acceso a Datos (`datos.py`)**: Administra los datos en memoria (simulación de una base de datos).

## Ventajas observadas respecto a la versión monolítica:

- **Mayor claridad**: cada parte del sistema está en su lugar, lo que hace el código más comprensible.
- **Mantenibilidad**: es más fácil modificar una sola parte (por ejemplo, cambiar la forma de almacenar los datos) sin tocar todo el sistema.
- **Reutilización**: la lógica puede ser usada por otras interfaces (por ejemplo, una API o app móvil).
- **Testing más simple**: se pueden probar las funciones de lógica o de datos por separado, sin necesidad de levantar el servidor.
