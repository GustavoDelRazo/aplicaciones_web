"""Framework web.py"""
import web

# Rutas de los controladores
urls = (
    '/', 'mvc.controllers.index.Index',
    '/ver','mvc.controllers.ver.Ver',
    '/borrar','mvc.controllers.borrar.Borrar',
    '/actualizar','mvc.controllers.actualizar.Actualizar',
    '/insertar','mvc.controllers.insertar.Insertar'
)
app = web.application(urls, globals())

        
# Punto de entrada 
if __name__ == "__main__":
    app.run()