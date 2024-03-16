import web
import base64  # Agrega esta línea
from mvc.models.productos import Productos

render = web.template.render('mvc/views/', base='layout')
productos_model = Productos()

class Insertar:
    def GET(self):
        return render.insertar()

    def POST(self):
        try:
            # Obtener los datos del formulario
            data = web.input()
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')
            precio = float(data.get('precio'))
            existencias = int(data.get('existencias'))

            # Obtener la imagen
            imagen = web.input(imagen={})
            imagen_data = imagen.imagen.file.read()
            # Codificar la imagen en base64
            imagen_base64 = base64.b64encode(imagen_data).decode('utf-8')

            # Insertar el producto en la base de datos
            productos_model.insert_product(nombre, descripcion, precio, existencias, imagen_base64)

            # Redirigir a la página de inicio después de la inserción
            raise web.seeother('/')
        except Exception as e:
            print("Error al mandar el producto:", e)
            return "Error al mandar el producto. Por favor, inténtelo de nuevo más tarde."
