import os
import mysql.connector

# Carga las variables de entorno desde el archivo .env
from dotenv import load_dotenv
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