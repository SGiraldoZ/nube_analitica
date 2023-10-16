INSERT INTO compras (id_curso, id_usuario, fecha, fecha_visualizacion, fecha_inicio, fecha_fin, interrupcion, longitud, latitud, id_plataforma, calificacion, costo_servicio)
VALUES
(1, 101, '2023-10-01 08:00:00', '2023-10-01 08:30:00', '2023-10-01 09:00:00', '2023-10-10 12:00:00', NULL, 40.7128, -74.0060, 1, 4, 49.99),
(2, 102, '2023-09-15 14:00:00', '2023-09-16 10:30:00', '2023-09-16 11:00:00', '2023-09-25 17:00:00', NULL, 34.0522, -118.2437, 1, 5, 59.99),
(3, 103, '2023-08-20 09:00:00', '2023-08-21 13:45:00', '2023-08-21 14:00:00', '2023-08-30 18:30:00', 'Interrupción técnica', 41.8781, -87.6298, 2, 4, 29.99),
(4, 104, '2023-07-05 11:30:00', '2023-07-06 08:15:00', '2023-07-06 08:30:00', '2023-07-15 14:45:00', NULL, 51.5074, -0.1278, 3, 3, 39.99),
(5, 105, '2023-06-10 10:15:00', '2023-06-11 10:30:00', '2023-06-11 11:00:00', '2023-06-20 15:30:00', NULL, 35.682839, 139.759455, 2, 5, 49.99),
(6, 106, '2023-05-19 15:30:00', '2023-05-20 09:45:00', '2023-05-20 10:00:00', '2023-05-29 13:30:00', NULL, 48.8566, 2.3522, 1, 4, 44.99),
(7, 107, '2023-04-25 12:00:00', '2023-04-26 14:30:00', '2023-04-26 15:00:00', '2023-05-05 17:15:00', 'Problema de conectividad', 52.5200, 13.4050, 3, 3, 34.99),
(8, 108, '2023-03-01 15:30:00', '2023-03-02 09:45:00', '2023-03-02 10:00:00', '2023-03-11 14:30:00', NULL, 48.8566, 2.3522, 2, 4, 44.99),
(9, 109, '2023-02-05 12:00:00', '2023-02-06 14:30:00', '2023-02-06 15:00:00', '2023-02-15 17:15:00', 'Problema de conectividad', 40.7128, -74.0060, 3, 3, 34.99),
(10, 110, '2023-01-15 10:00:00', '2023-01-16 08:15:00', '2023-01-16 08:30:00', '2023-01-25 12:45:00', NULL, 34.0522, -118.2437, 1, 5, 59.99),
(11, 111, '2022-12-20 09:45:00', '2022-12-21 13:00:00', '2022-12-21 13:15:00', '2022-12-30 16:30:00', 'Interrupción técnica', 41.8781, -87.6298, 2, 4, 29.99),
(12, 112, '2022-11-05 13:30:00', '2022-11-06 09:45:00', '2022-11-06 10:00:00', '2022-11-15 14:30:00', NULL, 51.5074, -0.1278, 3, 3, 39.99),
(13, 113, '2022-10-10 10:15:00', '2022-10-11 10:30:00', '2022-10-11 11:00:00', '2022-10-20 15:15:00', NULL, 35.682839, 139.759455, 1, 5, 49.99);

-- Insertar registros de prueba en la tabla "cursos"
INSERT INTO cursos (categoria, nombre) VALUES
('Programación', 'Introducción a la Programación en Python'),
('Programación', 'Fundamentos de Java'),
('Diseño Web', 'Diseño Web HTML/CSS'),
('Programación', 'Programación en C++'),
('Desarrollo de Aplicaciones', 'Desarrollo de Aplicaciones Móviles'),
('Idiomas', 'Inglés para Negocios'),
('Programación', 'Programación en JavaScript'),
('Robótica', 'Introducción a la Robótica');

-- Registros corregidos
INSERT INTO clientes (id_usuario, ciudad, pais, n_doc_cliente, email_cliente, nombre_cliente, fecha_nacimiento) VALUES
(101, 'Nueva York', 'Estados Unidos', NULL, 'cliente1@example.com', 'Cliente Uno', '1990-05-15'),
(102, 'Los Ángeles', 'Estados Unidos', NULL, 'cliente2@example.com', 'Cliente Dos', '1985-12-10'),
(103, 'Bogotá', 'Colombia', NULL, 'cliente3@example.com', 'Cliente Tres', '1980-09-22'),
(104, 'Medellín', 'Colombia', NULL, 'cliente4@example.com', 'Cliente Cuatro', '1995-03-30'),
(105, 'Barranquilla', 'Colombia', NULL, 'cliente5@example.com', 'Cliente Cinco', '1987-11-02'),
(106, 'Cartagena', 'Colombia', NULL, 'cliente6@example.com', 'Cliente Seis', '1989-07-18'),
(107, 'Santa Marta', 'Colombia', NULL, 'cliente7@example.com', 'Cliente Siete', '1983-02-25'),
(108, 'Cali', 'Colombia', NULL, 'cliente8@example.com', 'Cliente Ocho', '1992-11-12'),
(109, 'Bucaramanga', 'Colombia', NULL, 'cliente9@example.com', 'Cliente Nueve', '1988-06-08'),
(110, 'Miami', 'Estados Unidos', NULL, 'cliente10@example.com', 'Cliente Diez', '1991-04-04');