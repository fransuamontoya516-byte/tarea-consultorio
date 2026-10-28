CREATE DATABASE IF NOT EXISTS Consultorio;
USE Consultorio;

-- Tabla Pacientes
CREATE TABLE IF NOT EXISTS pacientes (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    DNI VARCHAR(10) NOT NULL UNIQUE,
    NOMBRE VARCHAR(100) NOT NULL,
    APELLIDO VARCHAR(100) NOT NULL,
    FECHA_DE_NACIMIENTO DATE NOT NULL,
    CELULAR VARCHAR(15) NOT NULL
);

-- Tabla Citas
CREATE TABLE IF NOT EXISTS citas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    ID_PACIENTE INT NOT NULL,
    FECHA DATE NOT NULL,
    HORA TIME NOT NULL,
    PRE_DIAGNOSTICO TEXT,
    ESTADO ENUM('en espera', 'atendido') DEFAULT 'en espera',
    FOREIGN KEY (ID_PACIENTE) REFERENCES pacientes(ID) ON DELETE CASCADE
);

-- Insertar 20 Registros en Pacientes
INSERT INTO pacientes (DNI, NOMBRE, APELLIDO, FECHA_DE_NACIMIENTO, CELULAR) VALUES
('10000001', 'Juan', 'Pérez', '1990-05-12', '912345601'),
('10000002', 'Maria', 'Gomez', '1985-08-22', '912345602'),
('10000003', 'Carlos', 'Lopez', '1992-11-03', '912345603'),
('10000004', 'Ana', 'Torres', '1998-01-15', '912345604'),
('10000005', 'Luis', 'Ramirez', '1980-03-30', '912345605'),
('10000006', 'Laura', 'Flores', '1995-07-19', '912345606'),
('10000007', 'Diego', 'Sanchez', '2000-12-05', '912345607'),
('10000008', 'Sofia', 'Diaz', '1993-04-18', '912345608'),
('10000009', 'Jorge', 'Vasquez', '1987-09-25', '912345609'),
('10000010', 'Elena', 'Rojas', '1991-06-14', '912345610'),
('10000011', 'Pedro', 'Mendoza', '1984-02-28', '912345611'),
('10000012', 'Lucia', 'Castillo', '1999-10-10', '912345612'),
('10000013', 'Mateo', 'Espinosa', '2001-08-08', '912345613'),
('10000014', 'Camila', 'Vargas', '1996-05-04', '912345614'),
('10000015', 'Gabriel', 'Cruz', '1989-11-20', '912345615'),
('10000016', 'Paula', 'Navarro', '1994-01-09', '912345616'),
('10000017', 'Daniel', 'Morales', '1982-07-07', '912345617'),
('10000018', 'Valeria', 'Ortiz', '1997-03-17', '912345618'),
('10000019', 'Hugo', 'Gutierrez', '1991-12-30', '912345619'),
('10000020', 'Andrea', 'Reyes', '2002-04-22', '912345620');

-- Insertar 20 Registros en C