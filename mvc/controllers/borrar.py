import web
from mvc.models.productos import Productos

render = web.template.render('mvc/views/', base='layout')
productos_model = Productos()

class Borrar:
    def GET(self):
        try:
            # Obtener el ID del producto de la URL
            params = web.input()
            producto_id = int(params.get('id'))
            
            # Obtener detalles del producto por ID
            producto = productos_model.get_product_by_id(producto_id)
            
            if producto:
                # Renderizar la página de confirmación de eliminación con los detalles del producto
                return render.borrar(producto=producto)
            else:
                return "Producto no encontrado."
        except Exception as e:
            print("Error al borrar el producto:", e)
            return "Error al borrar el producto. Por favor, inténtelo de nuevo más tarde."

    def POST(self):
        try:
            # Obtener el ID del producto del formulario
            data = web.input()
            producto_id = int(data.get('id'))
            
            # Eliminar el producto por ID
            productos_model.delete_product_by_id(producto_id)
            
            # Redirigir a la página de inicio después de la eliminación
            raise web.seeother('/')
        except Exception as e:
            print("Error al borrar el producto:", e)
            return "Error al borrar el producto. Por favor, inténtelo de nuevo más tarde."
