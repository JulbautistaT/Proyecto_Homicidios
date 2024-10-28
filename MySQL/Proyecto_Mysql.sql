CREATE DATABASE Homicidios;

USE Homicidios;

CREATE TABLE lugar_accidente (
    id_lugar INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    departamento VARCHAR(100) NOT NULL,
    municipio VARCHAR(100) NOT NULL
);

CREATE TABLE persona (
   id_persona INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
   genero VARCHAR(50),
   grupo_etario VARCHAR(50)
);

CREATE TABLE accidente (
    id_accidente INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    armas_medio VARCHAR(100),
    fecha_hecho DATE,
    cantidad_accidentes INT CHECK (cantidad_accidentes >= 0),
    id_lugar INT,
    id_persona INT,
    FOREIGN KEY(id_lugar) REFERENCES lugar_accidente(id_lugar),
    FOREIGN KEY(id_persona) REFERENCES persona(id_persona)
);

ALTER TABLE datos_inicio
MODIFY COLUMN Departamento VARCHAR(100),
MODIFY COLUMN Municipio VARCHAR(100),
MODIFY COLUMN Armas_medios VARCHAR(100),
MODIFY COLUMN Fecha_hecho DATE,
MODIFY COLUMN Genero VARCHAR(50),
MODIFY COLUMN Grupo_etario VARCHAR(50),
MODIFY COLUMN Cantidad INT;

INSERT INTO lugar_accidente (departamento, municipio)
SELECT Departamento, Municipio
FROM datos_inicio;

-- Verificar la inserción de los datos
SELECT * FROM lugar_accidente;

INSERT INTO persona (genero, grupo_etario)
SELECT genero, grupo_etario
FROM datos_inicio;

-- Verificar la inserción de los datos
SELECT * FROM persona;

INSERT INTO accidente (armas_medio, fecha_hecho, cantidad_accidentes, id_lugar, id_persona)
SELECT 
    di.Armas_medios,
    di.Fecha_hecho,
    di.Cantidad,
    (SELECT la.id_lugar FROM lugar_accidente la 
        WHERE la.departamento = di.Departamento 
        AND la.municipio = di.Municipio LIMIT 1),
    (SELECT p.id_persona FROM persona p 
        WHERE p.genero = di.Genero 
        AND p.grupo_etario = di.Grupo_etario LIMIT 1)
FROM datos_inicio di;

-- Verificar los datos de la tabla accidente
SELECT * FROM accidente;

SELECT * FROM datos_inicio;
SELECT * FROM lugar_accidente;

-- Renombrar algunos datos que tenían una mala escritura
UPDATE accidente
SET armas_medio = 'No reportado'
WHERE armas_medio = 'No repotado';

