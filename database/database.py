import os
import mysql.connector
from dotenv import load_dotenv
from model.user import User

# Carga las variables de entorno desde el archivo .env
load_dotenv()

# Obtiene los valores de las variables de entorno
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Crea la conexión a la base de datos
db_connection = mysql.connector.connect(
    host=db_host,
    port=db_port,
    user=db_user,
    password=db_password,
    database=db_name
)

# Crea un cursor para ejecutar consultas SQL
db_cursor = db_connection.cursor()

def insert_user(user):
    try:
        # Realiza la inserción en la base de datos
        query = "INSERT INTO Persona (Nombre, Apellido, Fecha_Nacimiento, Genero, Direccion, Telefono, Correo_Electronico, Numero_Identificacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (user.nombre, user.apellido, user.fecha_nacimiento, user.genero, user.direccion, user.telefono, user.correo_electronico, user.numero_identificacion)

        db_cursor.execute(query, values)
        db_connection.commit()

        # Retorna el ID del usuario recién insertado
        return db_cursor.lastrowid
    except Exception as e:
        # Manejo de errores
        print("Error al insertar usuario:", str(e))
        db_connection.rollback()
