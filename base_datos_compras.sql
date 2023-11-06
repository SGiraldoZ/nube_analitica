CREATE TABLE cursos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL
);


CREATE TABLE compras (
  id_compra INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_curso INT NOT NULL,
  id_usuario INT NOT NULL,
  fecha DATETIME NOT NULL,
  fecha_visualizacion DATETIME NOT NULL,
  fecha_inicio DATETIME NOT NULL,
  fecha_fin DATETIME NOT NULL,
  interrupcion VARCHAR(255) NULL,
  longitud FLOAT NULL,
  latitud FLOAT NULL,
  id_plataforma INT,
  calificacion INT NULL,
  costo_servicio FLOAT NULL
);

CREATE TABLE clientes (
  id_cliente INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT NOT NULL,
  ciudad VARCHAR(255),
  pais VARCHAR(255) NOT NULL,
  n_doc_cliente VARCHAR(255) NULL,
  email_cliente VARCHAR(255) NOT NULL,
  nombre_cliente VARCHAR(255) NOT NULL,
  fecha_nacimiento DATE NOT NULL  
);


