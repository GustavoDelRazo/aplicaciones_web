CREATE TABLE productos (
    id INTEGER PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Descripcion TEXT NOT NULL,
    Precio DECIMAL(10, 2) NOT NULL CHECK (Precio >= 0),
    Existencias INT NOT NULL CHECK (Existencias >= 0),
    Imagen TEXT
);


INSERT INTO productos (Nombre, Descripcion, Precio, Existencias)
VALUES ('Producto 1', 'Descripción 1', 1, 1),
       ('Producto 2', 'Descripción 2', 2, 2),
       ('Producto 3', 'Descripción 3', 3, 3);
