Use alcaldiareconfacial_db;

CREATE TABLE Persona (
    ID_Persona INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255) NOT NULL, 
    Apellido VARCHAR(255) NOT NULL, 
    Fecha_Nacimiento DATE, 
    Genero VARCHAR(255), 
    Direccion VARCHAR(255), 
    Telefono VARCHAR(50),
    Correo_Electronico VARCHAR(255) UNIQUE, 
    Numero_Identificacion VARCHAR(255) UNIQUE 
);

CREATE TABLE Empleado (
    ID_Empleado INT AUTO_INCREMENT PRIMARY KEY,
    ID_Persona INT, 
    Cargo VARCHAR(255),
    Departamento VARCHAR(255),
    FOREIGN KEY (ID_Persona) REFERENCES Persona(ID_Persona)
);

CREATE TABLE Cliente (
    ID_Cliente INT AUTO_INCREMENT PRIMARY KEY,
    ID_Persona INT, 
    Tipo_Cliente VARCHAR(50),
    FOREIGN KEY (ID_Persona) REFERENCES Persona(ID_Persona)
);

CREATE TABLE Acceso (
    ID_Acceso INT AUTO_INCREMENT PRIMARY KEY,
    ID_Persona INT, 
    Fecha_Hora_Entrada DATETIME,
    Fecha_Hora_Salida DATETIME,
    ID_Sistema_Reconocimiento INT, 
    FOREIGN KEY (ID_Persona) REFERENCES Persona(ID_Persona),
    FOREIGN KEY (ID_Sistema_Reconocimiento) REFERENCES Sistema_Reconocimiento_Facial(ID_Sistema)
);

CREATE TABLE Sistema_Reconocimiento_Facial (
    ID_Sistema INT AUTO_INCREMENT PRIMARY KEY,
    Nombre_Sistema VARCHAR(255),
    Especificaciones_Tecnicas VARCHAR(255),
    Fabricante VARCHAR(255),
    Fecha_Instalacion DATE,
    Ubicacion_Sistema VARCHAR(255) 
);

