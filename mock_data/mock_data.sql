-- Insertar registros de prueba en la tabla "cursos"
INSERT INTO cursos (categoria, nombre) VALUES
('Diseño', 'Diseño de Experiencia de Usuario (UX)'),
('Salud', 'Nutrición y Salud'),
('Fotografía', 'Fotografía Digital'),
('Arte', 'Introducción a la Historia del Arte'),
('Redacción', 'Redacción Creativa'),
('Desarrollo de Aplicaciones', 'Desarrollo de Aplicaciones Móviles para Android'),
('Marketing', 'Marketing de Contenidos'),
('Ciencias', 'Introducción a la Biología'),
('Programación', 'Programación en Ruby'),
('Idiomas', 'Inglés Intermedio'),
('Ciencias', 'Introducción a la Astronomía');


INSERT INTO compras (id_curso, id_usuario, fecha, fecha_visualizacion, fecha_inicio, fecha_fin, interrupcion, longitud, latitud, id_plataforma, calificacion, costo_servicio)
VALUES
(48, 148, '2022-01-20 14:45:00', '2022-01-21 12:00:00', '2022-01-21 12:15:00', '2022-01-30 16:45:00', 'Interrupción técnica', 41.8781, -87.6298, 2, 3, 29.99),
(49, 149, '2021-12-03 13:15:00', '2021-12-04 10:30:00', '2021-12-04 11:00:00', '2021-12-13 14:30:00', NULL, 51),
(54, 154, '2023-03-08 10:00:00', '2023-03-09 09:15:00', '2023-03-09 09:30:00', '2023-03-18 11:45:00', NULL, 40.7128, -74.0060, 2, 5, 59.99),
(55, 155, '2023-02-15 09:30:00', '2023-02-16 08:45:00', '2023-02-16 09:00:00', '2023-02-25 12:30:00', NULL, 34.0522, -118.2437, 1, 4, 49.99),
(56, 156, '2023-01-20 14:45:00', '2023-01-21 12:00:00', '2023-01-21 12:15:00', '2023-01-30 16:45:00', 'Interrupción técnica', 41.8781, -87.6298, 2, 3, 29.99),
(57, 157, '2022-12-03 13:15:00', '2022-12-04 10:30:00', '2022-12-04 11:00:00', '2022-12-13 14:30:00', NULL, 51.5074, -0.1278, 3, 4, 39.99),
(58, 158, '2022-11-17 10:45:00', '2022-11-18 10:00:00', '2022-11-18 10:15:00', '2022-11-27 15:00:00', NULL, 35.682839, 139.759455, 2, 5, 44.99),
(59, 159, '2022-10-25 11:30:00', '2022-10-26 15:00:00', '2022-10-26 15:30:00', '2022-11-04 17:45:00', 'Problema de conectividad', 52.5200, 13.4050, 1, 3, 34.99);

