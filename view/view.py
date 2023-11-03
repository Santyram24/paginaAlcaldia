import sys
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from model.user_model import User
from model.reconocimiento_model import RecognitionLog
from services.reconocimiento_facial import compare_facial_images, capture_facial_image
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class RegistrationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Registro y Autenticación con Reconocimiento Facial")
        self.setGeometry(100, 100, 600, 400)

        # Configura el fondo azul utilizando una hoja de estilo
        style = """
            QMainWindow {
                background-color: #3498db;
            }
            
            QLabel {
                color: white;
            }
           
            QPushButton {
                background-color: #27ae60;
                color: white;
                border: 2px solid #27ae60;
                border-radius: 5px;
                height: 40px;
            }
            QLineEdit {
                border: 2px solid #3498db;
                border-radius: 5px;
                height: 40px;
            }
        """
        self.setStyleSheet(style)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        # Widgets para el registro
        username_label = QLabel("Nombre de Usuario")
        self.username_input = QLineEdit()
        password_label = QLabel("Contraseña")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        register_button = QPushButton("Registrar")
        register_button.clicked.connect(self.register_user)

        # Crear un QLabel para la imagen
        image_label = QLabel(self)
        pixmap = QPixmap('view/img/Granada.jpg')  # Asegúrate de tener la imagen en la ubicación correcta
        pixmap = pixmap.scaled(100, 120, Qt.KeepAspectRatio)  # Redimensionar la imagen
        image_label.setPixmap(pixmap)

        # Crear un layout horizontal para la imagen
        image_layout = QVBoxLayout()
        image_layout.addStretch(1)  # Espacio en blanco a la izquierda de la imagen
        image_layout.addWidget(image_label)  # Agregar la imagen
        image_layout.addStretch(1)  # Espacio en blanco a la derecha de la imagen

        # Widgets para la autenticación
        auth_username_label = QLabel("Nombre de Usuario")
        self.auth_username_input = QLineEdit()
        auth_password_label = QLabel("Contraseña")
        self.auth_password_input = QLineEdit()
        self.auth_password_input.setEchoMode(QLineEdit.Password)
        authenticate_button = QPushButton("Ingresar")
        authenticate_button.clicked.connect(self.authenticate_user)

        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(register_button)
        layout.addLayout(image_layout)
        layout.addWidget(auth_username_label)
        layout.addWidget(self.auth_username_input)
        layout.addWidget(auth_password_label)
        layout.addWidget(self.auth_password_input)
        layout.addWidget(authenticate_button)

        central_widget.setLayout(layout)

    def register_user(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if not username or not password:
            return  # Validación de entrada

        user = User(username, password)
        self.save_user_data(user)
        self.capture_and_save_facial_image(username)

    def save_user_data(self, user):
        username = user.username
        password = user.password
        user_data_file = "user_data.txt"

        with open(user_data_file, "a") as file:
            file.write(f"Usuario: {username}, Contraseña: {password}\n")

    def capture_and_save_facial_image(self, username):
        image_path = capture_facial_image()
        if image_path:
            recognition_log = RecognitionLog(username, image_path)
            self.save_recognition_log(recognition_log)

    def save_recognition_log(self, recognition_log):
        username = recognition_log.username
        image_path = recognition_log.image_path
        recognition_log_file = "recognition_log.txt"

        with open(recognition_log_file, "a") as file:
            file.write(f"Usuario: {username}, Ruta de la imagen: {image_path}\n")

    def authenticate_user(self):
        username = self.auth_username_input.text()
        password = self.auth_password_input.text()

        if not username or not password:
            return  # Validación de entrada

        if self.verify_user_credentials(username, password):
            recognition_log = self.get_recognition_log_by_username(username)
            
            if recognition_log:
                cap = cv2.VideoCapture(0)  # Iniciar la captura de la cámara

                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    if compare_facial_images(frame, recognition_log.image_path):
                        self.show_authentication_result("Autenticación facial exitosa.")
                        break
                    else:
                        self.show_authentication_result("Fallo en la autenticación facial.")

                    # Mostrar el frame de la cámara en la interfaz gráfica
                    self.display_camera_frame(frame)

                cap.release()  # Detener la captura de la cámara
            else:
                self.show_authentication_result("Fallo en la recuperación del registro de reconocimiento.")
        else:
            self.show_authentication_result("Credenciales de usuario no válidas.")

    def verify_user_credentials(self, username, password):
        # Esta función debería consultar una base de datos o archivo para verificar las credenciales del usuario.
        # En este ejemplo, solo se simula la verificación.
        return True

    def get_recognition_log_by_username(self, username):
        # Esta función debería consultar una base de datos o archivo para obtener el registro de reconocimiento del usuario.
        # En este ejemplo, solo se simula la recuperación.
        image_path = "/captured_images"  # Reemplaza con la ubicación real de la imagen
        return RecognitionLog(username, image_path)

    def show_authentication_result(self, message):
        # Muestra el resultado de la autenticación en la interfaz gráfica
        # Puedes usar un QLabel o QMessageBox para mostrar el mensaje.
        pass

    def display_camera_frame(self, frame):
        # Muestra el frame de la cámara en la interfaz gráfica (por ejemplo, en un QLabel)
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = RegistrationApp()
    window.show()
    sys.exit(app.exec_())