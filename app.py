import sys
from PyQt5.QtWidgets import QApplication
from view.view import RegistrationApp


def main():
    app = QApplication(sys.argv)
    window = RegistrationApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    
    # interfaz y funcionalidad