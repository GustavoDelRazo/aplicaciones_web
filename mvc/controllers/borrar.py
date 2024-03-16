import web
from mvc.models.productos import Productos

render = web.template.render('mvc/views/', base='layout')
productos_model = Productos()

class Borrar:
    def GET(self):
        try:
            
            params = web.input()
            producto_id = int(params.get('id'))
            
            producto = productos_model.get_product_by_id(producto_id)
            
            if producto:
                
                return render.borrar(producto=producto)
            else:
                return "Producto no encontrado."
        except Exception as e:
            print("Error al borrar el producto:", e)
            return "Error al borrar el producto. Por favor, inténtelo de nuevo más tarde."

    def POST(self):
        try:
           
            data = web.input()
            producto_id = int(data.get('id'))
            
            productos_model.delete_product_by_id(producto_id)
            
            raise web.seeother('/')
        except Exception as e:
            print("Error al borrar el producto:", e)
            return "Error al borrar el producto. Por favor, inténtelo de nuevo más tarde."
