CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL CHECK (Precio >= 0),
    Existencias INT NOT NULL CHECK (Existencias >= 0),
    Imagen TEXT
);


INSERT INTO productos (Nombre, Descripcion, Precio, Existencias)
VALUES ('Producto 1', 'Descripción del producto 1', 19.99, 50),
       ('Producto 2', 'Descripción del producto 2', 29.99, 100),
       ('Producto 3', 'Descripción del producto 3', 39.99, 75);
