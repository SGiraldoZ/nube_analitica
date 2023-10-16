INSERT INTO cursos (categoria, nombre) VALUES
('Tecnología', 'Ciencia de Datos con Python'),
('Diseño de Videojuegos', 'Diseño de Videojuegos'),
('Cocina', 'Aprende a Cocinar Sushi'),
('Salud', 'Yoga y Meditación'),
('Programación', 'Programación en PHP'),
('Psicología', 'Introducción a la Psicología'),
('Marketing', 'Marketing en Redes Sociales'),
('Ciencias', 'Introducción a la Astronomía'),
('Arte', 'Pintura al Óleo'),
('Idiomas', 'Alemán Básico'),
('Programación', 'Programación en C#');


INSERT INTO compras (id_curso, id_usuario, fecha, fecha_visualizacion, fecha_inicio, fecha_fin, interrupcion, longitud, latitud, id_plataforma, calificacion, costo_servicio)
VALUES
(1, 114, '2022-09-15 14:00:00', '2022-09-16 08:30:00', '2022-09-16 09:00:00', '2022-09-25 12:30:00', 'Problema de conectividad', 48.8566, 2.3522, 2, 4, 44.99),
(5, 115, '2022-08-25 12:45:00', '2022-08-26 11:00:00', '2022-08-26 11:15:00', '2022-09-04 15:30:00', NULL, 40.7128, -74.0060, 1, 3, 34.99),
(6, 116, '2022-07-30 10:30:00', '2022-07-31 13:45:00', '2022-07-31 14:00:00', '2022-08-09 16:45:00', 'Interrupción técnica', 34.0522, -118.2437, 3, 4, 39.99),
(7, 117, '2022-06-10 11:00:00', '2022-06-11 09:15:00', '2022-06-11 09:30:00', '2022-06-20 14:30:00', NULL, 41.8781, -87.6298, 1, 5, 59.99),
(8, 118, '2022-05-20 09:15:00', '2022-05-21 08:30:00', '2022-05-21 09:00:00', '2022-05-30 12:45:00', 'Problema de conectividad', 51.5074, -0.1278, 2, 4, 29.99),
(9, 119, '2022-04-25 13:45:00', '2022-04-26 09:30:00', '2022-04-26 10:00:00', '2022-05-05 14:15:00', NULL, 35.682839, 139.759455, 3, 3, 49.99),
(11, 120, '2022-03-15 15:00:00', '2022-03-16 13:15:00', '2022-03-16 13:30:00', '2022-03-25 17:45:00', NULL, 52.5200, 13.4050, 1, 4, 39.99),
(6, 146, '2022-03-08 10:00:00', '2022-03-09 09:15:00', '2022-03-09 09:30:00', '2022-03-18 11:45:00', NULL, 40.7128, -74.0060, 2, 5, 59.99),
(2, 147, '2022-02-15 09:30:00', '2022-02-16 08:45:00', '2022-02-16 09:00:00', '2022-02-25 12:30:00', NULL, 34.0522, -118.2437, 1, 4, 49.99);


-- Registros de clientes del 11 al 20 con abreviaciones de país y ciudad
INSERT INTO clientes (id_usuario, ciudad, pais, n_doc_cliente, email_cliente, nombre_cliente, fecha_nacimiento) VALUES
(111, 'NY', 'US', NULL, 'cliente11@example.com', 'Cliente Once', '1981-08-29'),
(112, 'LA', 'US', NULL, 'cliente12@example.com', 'Cliente Doce', '1993-10-16'),
(113, 'BO', 'CO', NULL, 'cliente13@example.com', 'Cliente Trece', '1986-03-09'),
(114, 'ME', 'CO', NULL, 'cliente14@example.com', 'Cliente Catorce', '1984-12-20'),
(115, 'BA', 'CO', NULL, 'cliente15@example.com', 'Cliente Quince', '1982-01-07'),
(116, 'CA', 'CO', NULL, 'cliente16@example.com', 'Cliente Dieciséis', '1989-04-15'),
(117, 'SA', 'CO', NULL, 'cliente17@example.com', 'Cliente Diecisiete', '1987-05-23'),
(118, 'CA', 'US', NULL, 'cliente18@example.com', 'Cliente Dieciocho', '1990-07-12'),
(119, 'MI', 'US', NULL, 'cliente19@example.com', 'Cliente Diecinueve', '1985-02-28'),
(120, 'DA', 'CO', NULL, 'cliente20@example.com', 'Cliente Veinte', '1992-11-03');
