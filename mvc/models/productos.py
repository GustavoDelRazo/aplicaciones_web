import sqlite3

class Productos:
    def get_total_products(self):
        try:
            # Conexión a la base de datos
            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            # Consulta para obtener el número total de productos
            c.execute("SELECT COUNT(*) FROM productos")
            # Obtener el resultado
            total_productos = c.fetchone()[0]
            # Cerrar conexión
            conn.close()
            return total_productos
        except sqlite3.Error as e:
            print("Error al obtener el número total de productos:", e)
            return 0

    def get_product_by_id(self, producto_id):
        try:
            # Conexión a la base de datos
            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            # Consulta para obtener los detalles del producto por su ID
            c.execute("SELECT * FROM productos WHERE id=?", (producto_id,))
            # Obtener el resultado
            productos = c.fetchone()
            # Cerrar conexión
            conn.close()
            return productos
        except sqlite3.Error as e:
            print("Error al obtener los detalles del producto:", e)
            return None        


    def get_products_paginated(self, start, limit):
        try:
            # Conexión a la base de datos
            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            # Consulta para obtener los productos paginados
            c.execute("SELECT * FROM productos LIMIT ?, ?", (start, limit))
            # Obtener los resultados
            productos = c.fetchall()
            # Cerrar conexión
            conn.close()
            return productos
        except sqlite3.Error as e:
            print("Error al obtener productos paginados:", e)
            return None
        

    def delete_product_by_id(self, producto_id):
        try:
            # Conexión a la base de datos
            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            # Consulta para eliminar el producto por ID
            c.execute("DELETE FROM productos WHERE id=?", (producto_id,))
            # Confirmar la transacción
            conn.commit()
            # Cerrar conexión
            conn.close()
        except sqlite3.Error as e:
            print("Error al eliminar el producto:", e)

    def update_product_with_image(self, producto_id, nombre, descripcion, precio, existencias, imagen):
        try:
            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            # Consulta para actualizar el producto con imagen por ID
            c.execute("UPDATE productos SET Nombre=?, Descripcion=?, Precio=?, Existencias=?, Imagen=? WHERE id=?", (nombre, descripcion, precio, existencias, imagen, producto_id))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Error al actualizar el producto con imagen:", e)


    def insert_product(self, nombre, descripcion, precio, existencias, imagen):
        try:
            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            c.execute("INSERT INTO productos (Nombre, Descripcion, Precio, Existencias, Imagen) VALUES (?, ?, ?, ?, ?)",
                    (nombre, descripcion, precio, existencias, imagen))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Error al insertar el producto:", e)

    def search_products(self, term):
        try:
            # Conexión a la base de datos
            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            # Consulta para buscar productos por nombre o descripción
            c.execute("SELECT * FROM productos WHERE Nombre LIKE ? OR Descripcion LIKE ?", ('%'+term+'%', '%'+term+'%'))
            # Obtener los resultados
            productos = c.fetchall()
            # Cerrar conexión
            conn.close()
            return productos
        except sqlite3.Error as e:
            print("Error al buscar productos:", e)
            return None