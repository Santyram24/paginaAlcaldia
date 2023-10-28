import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QFrame, QSplitter
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from database import insert_user_image  # Importa una función que guarda la imagen del usuario en la base de datos
import cv2

# Función para capturar una imagen facial
def capture_facial_image():
    cap = cv2.VideoCapture(0)  # Usa la cámara predeterminada (cambiar a la cámara correcta si es necesario)
    
    # Captura un solo frame
    ret, frame = cap.read()
    
    if ret:
        # Guarda la imagen capturada
        image_path = "captured_face.jpg"  # Cambia la ubicación y el nombre del archivo si es necesario
        cv2.imwrite(image_path, frame)
        cap.release()
        return image_path
    else:
        cap.release()
        return None

def signup():
    # Captura la imagen facial
    image_path = capture_facial_image()

    if image_path:
        # Agrega aquí la lógica para el registro facial
        # Llama a la función insert_user_image con la imagen capturada
        username = usuario_entrada.text()
        insert_user_image(username, image_path)
        print("Registro Facial exitoso")
    else:
        print("Error al capturar la imagen facial")

# En tu base de datos.py (o archivo adecuado), implementa la función insert_user_image
# Asegúrate de reemplazar con tu propia lógica de inserción en la base de datos

def insert_user_image(username, image_path):
    try:
        # Abre la imagen y léela como datos binarios
        with open(image_path, "rb") as image_file:
            image_binary = image_file.read()

        # Inserta la imagen en la base de datos
        print(f"Guardando imagen facial de {username} en la base de datos")

        # Reemplaza con tu lógica de inserción a la base de datos
        # Usar la variable "username" para identificar al usuario
    except Exception as e:
        print("Error al guardar la imagen en la base de datos:", str(e))

# ...

if _name_ == "_main_":
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    ventana.setWindowTitle("Registro")
    ventana.setGeometry(100, 100, 1000, 600)

    layout = QVBoxLayout()

    # ...

    ventana.show()
    sys.exit(app.exec_())