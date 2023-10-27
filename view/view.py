import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont  # Importa QFont
from PyQt5.QtCore import Qt  # Importa Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout,QFrame, QWidget,QSplitter


def signup():
    # Agrega aquí la lógica para el registro facial
    print("Registro Facial")

def login():
    # Agrega aquí la lógica para el inicio de sesión
    print("Inicio de Sesión")

def pantalla_principal():
    app = QApplication(sys.argv)
    ventana = QMainWindow()
    ventana.setWindowTitle("Registro")
    ventana.setGeometry(100, 100, 1000, 600)  # Aumenta el ancho de la ventana

    layout = QVBoxLayout()

    left_widget = QWidget()  # Widget contenedor para el grupo de registro
    left_layout = QVBoxLayout(left_widget)
    usuario_label = QLabel("Usuario *")
    usuario_entrada = QLineEdit()
    usuario_label.setBuddy(usuario_entrada)

    contra_label = QLabel("Contraseña *")
    contra_entrada = QLineEdit()
    contra_label.setBuddy(contra_entrada)

    boton_registro_facial = QPushButton("Registro Facial")
    boton_registro_facial.setStyleSheet("background-color: #3498db; color: white; border-radius: 5px; height: 50px;")
    boton_registro_facial.clicked.connect(signup)

    left_layout.addWidget(QLabel("Registro facial: debe asignar un usuario y contraseña:"))
    left_layout.addWidget(usuario_label)
    left_layout.addWidget(usuario_entrada)
    left_layout.addWidget(contra_label)
    left_layout.addWidget(contra_entrada)
    left_layout.addWidget(boton_registro_facial)

    right_widget = QWidget()  # Widget contenedor para el grupo de inicio de sesión
    right_layout = QVBoxLayout(right_widget)
    usuariologueo_label = QLabel("Usuario *")
    usuariologueo_entrada = QLineEdit()
    usuariologueo_label.setBuddy(usuariologueo_entrada)

    contralogueo_label = QLabel("Contraseña *")
    contralogueo_entrada = QLineEdit()
    contralogueo_label.setBuddy(contralogueo_entrada)

    boton_logueo = QPushButton("Inicio de Sesión")
    boton_logueo.setStyleSheet("background-color: #27ae60; color: white; border-radius: 5px; height: 50px;")
    boton_logueo.clicked.connect(login)

    right_layout.addWidget(QLabel("Inicio de sesion:"))
    right_layout.addWidget(usuariologueo_label)
    right_layout.addWidget(usuariologueo_entrada)
    right_layout.addWidget(contralogueo_label)
    right_layout.addWidget(contralogueo_entrada)
    right_layout.addWidget(boton_logueo)



    # Utiliza un QFrame como separador
    separator = QFrame()
    separator.setFrameShape(QFrame.VLine)  # Separador vertical
    separator.setFrameShadow(QFrame.Sunken)

    # Utiliza un QSplitter para la separación horizontal
    splitter = QSplitter()
    splitter.addWidget(left_widget)
    splitter.addWidget(separator)  # Agrega el separador
    splitter.addWidget(right_widget)
    left_widget.setMinimumWidth(200)
    right_widget.setMinimumWidth(200)


    layout.addWidget(splitter)
    # Ajusta los tamaños iniciales de los widgets (izquierda, separador, derecha)
    splitter.setSizes([1, 1, 1])


    central_widget = QWidget()
    central_widget.setLayout(layout)
    ventana.setCentralWidget(central_widget)

    ventana.show()
    sys.exit(app.exec_())

pantalla_principal()