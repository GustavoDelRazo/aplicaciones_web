import web
import sqlite3
import math

from mvc.models.productos import Productos

render = web.template.render('mvc/views/', base='layout')
productos_model = Productos()

class Index:
    def GET(self):
        try:
            total_productos = productos_model.get_total_products()
            productos_por_pagina = 6
            total_paginas = math.ceil(total_productos / productos_por_pagina)

            params = web.input(page=1)
            page = int(params.page)
            start = (page - 1) * productos_por_pagina
            end = start + productos_por_pagina

            productos = productos_model.get_products_paginated(start, productos_por_pagina)

            return render.index(productos=productos, page=page, total_paginas=total_paginas)
        except Exception as e:
            print("Error en la página de inicio:", e)
            return "Error en la página de inicio. Por favor, inténtelo de nuevo más tarde."


    def POST(self):
        try:
           
            form = web.input(search="")
            term = form.search.strip()

            if term:
                
                productos = productos_model.search_products(term)
            else:
                
                productos = productos_model.get_products_paginated(0, 6)

            return render.index(productos=productos, page=1, total_paginas=1)
        except Exception as e:
            print("Error en la búsqueda de productos:", e)
            return "Error en la búsqueda de productos. Por favor, inténtelo de nuevo más tarde."