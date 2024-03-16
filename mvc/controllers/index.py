import web
import sqlite3
import math

from mvc.models.productos import Productos

render = web.template.render('mvc/views/', base='layout')
productos_model = Productos()

class Index:
    def GET(self):
        try:
            # Obtener el número total de productos
            total_productos = productos_model.get_total_products()

            # Calcular el número total de páginas necesarias
            total_paginas = math.ceil(total_productos / 6)

            # Obtener el número de página solicitado
            params = web.input(page=1)
            page = int(params.page)

            # Calcular el índice de inicio y fin para la paginación
            start = (page - 1) * 6
            end = min(start + 6, total_productos)  # Limitar al número total de productos

            # Obtener los productos para la página actual
            productos = productos_model.get_products_paginated(start, end)

            return render.index(productos=productos, page=page, total_paginas=total_paginas)
        except Exception as e:
            print("Error en la página de inicio:", e)
            return "Error en la página de inicio. Por favor, inténtelo de nuevo más tarde."

    def POST(self):
        try:
            # Obtener el término de búsqueda del formulario
            form = web.input(search="")
            term = form.search.strip()

            if term:
                # Buscar productos por nombre o descripción
                productos = productos_model.search_products(term)
            else:
                # Si no se proporciona un término de búsqueda, mostrar todos los productos
                productos = productos_model.get_products_paginated(0, 6)

            return render.index(productos=productos, page=1, total_paginas=1)
        except Exception as e:
            print("Error en la búsqueda de productos:", e)
            return "Error en la búsqueda de productos. Por favor, inténtelo de nuevo más tarde."