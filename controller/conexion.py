import mysql.connector

try:
    # conexion base Cristian G
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="alcaldia"
    )

    print("Conexión exitosa a la base de datos.")

except mysql.connector.Error as error:
    print("No se pudo establecer la conexión a la base de datos: ", error)