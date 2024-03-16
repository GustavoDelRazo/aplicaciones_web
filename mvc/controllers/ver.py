import web
from mvc.models.productos import Productos

render = web.template.render('mvc/views/', base='layout')
productos_model = Productos()

class Ver:
    def GET(self):
        try:
            # Obtener el ID del producto de la URL
            params = web.input()
            producto_id = int(params.get('id'))
            
            # Obtener detalles del producto por ID
            producto = productos_model.get_product_by_id(producto_id)
            
            if producto:
                return render.ver(producto=producto)
            else:
                return "Producto no encontrado."
        except Exception as e:
            print("Error al mostrar el producto:", e)
            return "Error al mostrar el producto. Por favor, inténtelo de nuevo más tarde."
