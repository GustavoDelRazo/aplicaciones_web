import web
import base64
from mvc.models.productos import Productos

render = web.template.render('mvc/views/', base='layout')
productos_model = Productos()

class Actualizar:
    def GET(self):
        try:
            params = web.input()
            producto_id = int(params.get('id'))
            
            producto = productos_model.get_product_by_id(producto_id)
            
            if producto:
                return render.actualizar(producto=producto)
            else:
                return "Producto no encontrado."
        except Exception as e:
            print("Error al obtener el producto para actualizar:", e)
            return "Error al obtener el producto para actualizar. Por favor, inténtelo de nuevo más tarde."

    def POST(self):
        try:
            data = web.input()
            producto_id = int(data.get('id'))
            nombre = data.get('nombre')
            descripcion = data.get('descripcion')
            precio = float(data.get('precio'))
            existencias = int(data.get('existencias'))

            imagen = web.input(imagen={})
            imagen_data = imagen.imagen.file.read()
            imagen_base64 = base64.b64encode(imagen_data).decode('utf-8')

            if imagen_data:
                productos_model.update_product_with_image(producto_id, nombre, descripcion, precio, existencias, imagen_base64)
            else:
                producto = productos_model.get_product_by_id(producto_id)
                imagen_base64 = producto[5] if producto else None

                productos_model.update_product_with_image(producto_id, nombre, descripcion, precio, existencias, imagen_base64)

            raise web.seeother('/')
        except Exception as e:
            print("Error al actualizar el producto:", e)
            return "Error al actualizar el producto. Por favor, inténtelo de nuevo más tarde."
