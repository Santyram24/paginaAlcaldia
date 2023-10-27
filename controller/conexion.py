import mysql.connector

try:
    # conexion base Cristian Gonzalez
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="alcaldiareconfacial_db"
    )

    print("Conexión exitosa a la base de datos.")

except mysql.connector.Error as error:
    print("No se pudo establecer la conexión a la base de datos: ", error)