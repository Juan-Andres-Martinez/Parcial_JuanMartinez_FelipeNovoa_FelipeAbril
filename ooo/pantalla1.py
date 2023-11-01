from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class IniciSesion(QDialog):
    def __init__(self):
        super().__init__()

        """ Configurar la aplicación""" 
        self.setGeometry(100,200,200,200); 
        self.setWindowTitle("Inicio"); 
        self.show();#muestra la ventana en la panta lla

        layout = QVBoxLayout()

        self.username_label = QLabel('Correo')
        self.username_field = QLineEdit()

        self.password_label = QLabel('Contraseña')
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton('Entrar')


        self.login_button.clicked.connect(self.__init__)


        self.register_button = QPushButton('Registrarse')

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_field)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_field)
        layout.addWidget(self.login_button)     
        layout.addWidget(self.register_button)

        self.setLayout(layout)
    
   
        
if __name__ == '__main__': 
    app = QApplication([])
    
    login_dialog = IniciSesion()
    login_dialog.show()

    
    app.exec()