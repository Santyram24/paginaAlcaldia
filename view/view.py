import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from model.user_model import User
from model.reconocimiento_model import RecognitionLog
from services.reconocimiento_facial import capture_facial_image

class RegistrationApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Registro de Reconocimiento Facial")
        self.setGeometry(100, 100, 600, 300)

        # Configura el fondo azul utilizando una hoja de estilo
        style = "QMainWindow { background: #3498db; }"
        self.setStyleSheet(style)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        username_label = QLabel("Nombre de Usuario")
        self.username_input = QLineEdit()
        password_label = QLabel("Contraseña")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        register_button = QPushButton("Registrar")
        register_button.clicked.connect(self.register_user)

        layout.addWidget(username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(register_button)

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
        # Obtén los datos del usuario
        username = user.username
        password = user.password
    
        # Define la ruta del archivo donde se guardarán los datos de usuario
        user_data_file = "user_data.txt"

        # Abre el archivo en modo escritura (se creará si no existe)
        with open(user_data_file, "a") as file:
            # Escribe los datos del usuario en el archivo
            file.write(f"Usuario: {username}, Contraseña: {password}\n")

    def capture_and_save_facial_image(self, username):
        image_path = capture_facial_image()  # Utiliza la función de captura de imágenes del servicio facial_recognition_service
        if image_path:
            recognition_log = RecognitionLog(username, image_path)
            self.save_recognition_log(recognition_log)

    def save_recognition_log(self, recognition_log):
        # Obtén los datos del registro de reconocimiento
        username = recognition_log.username
        image_path = recognition_log.image_path
    
        # Define la ruta del archivo donde se guardarán los registros de reconocimiento
        recognition_log_file = "recognition_log.txt"

        # Abre el archivo en modo escritura (se creará si no existe)
        with open(recognition_log_file, "a") as file:
            # Escribe los datos del registro de reconocimiento en el archivo
            file.write(f"Usuario: {username}, Ruta de la imagen: {image_path}\n")
