import sqlite3

class Productos:
    def get_total_products(self):
        try:
            
            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM productos")
            total_productos = c.fetchone()[0]
            conn.close()
            return total_productos
        except sqlite3.Error as e:
            print("Error al obtener el número total de productos:", e)
            return 0


    def get_product_by_id(self, producto_id):
        try:

            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            c.execute("SELECT * FROM productos WHERE id=?", (producto_id,))
            productos = c.fetchone()
            conn.close()
            return productos
        except sqlite3.Error as e:
            print("Error al obtener los detalles del producto:", e)
            return None        


    def get_products_paginated(self, start, limit):
        try:

            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            c.execute("SELECT * FROM productos LIMIT ?, ?", (start, limit))
            productos = c.fetchall()
            conn.close()
            return productos
        except sqlite3.Error as e:
            print("Error al obtener productos paginados:", e)
            return None
        

    def delete_product_by_id(self, producto_id):
        try:
           
            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            c.execute("DELETE FROM productos WHERE id=?", (producto_id,))
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            print("Error al eliminar el producto:", e)


    def update_product_with_image(self, producto_id, nombre, descripcion, precio, existencias, imagen):
        try:

            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
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

            conn = sqlite3.connect('mvc/models/productos.db')
            c = conn.cursor()
            c.execute("SELECT * FROM productos WHERE Nombre LIKE ? OR Descripcion LIKE ?", ('%'+term+'%', '%'+term+'%'))
            productos = c.fetchall()
            conn.close()
            return productos
        except sqlite3.Error as e:
            print("Error al buscar productos:", e)
            return None