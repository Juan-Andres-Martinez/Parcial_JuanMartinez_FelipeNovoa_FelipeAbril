from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Registro(QDialog):
    def __init__(self):
        super().__init__()

        """ Configurar la aplicación""" 
        self.setGeometry(100,200,200,200); 
        self.setWindowTitle("Registar"); 
        self.show();#muestra la ventana en la pantalla

        layout = QVBoxLayout()

        self.name_label = QLabel('Nombres')
        self.name_field = QLineEdit()

        self.lastname_label = QLabel('Apellidos')
        self.lastname_field = QLineEdit()

        self.edad_label = QLabel('Edad')
        self.edad_field = QLineEdit()

        self.celular_label = QLabel('Celular')
        self.celular_field = QLineEdit()

        self.id_label = QLabel('Cedula')
        self.id_field = QLineEdit()
        
        self.email_label = QLabel('Correo')
        self.email_field = QLineEdit()

        self.password_label = QLabel('Contraseña')
        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.EchoMode.Password)

        
        self.register_button = QPushButton('Registrarse')
        self.login_button = QPushButton('Entrar')


        layout.addWidget(self.name_label)
        layout.addWidget(self.name_field)

        layout.addWidget(self.lastname_label)
        layout.addWidget(self.lastname_field)

        layout.addWidget(self.edad_label)
        layout.addWidget(self.edad_field)

        layout.addWidget(self.id_label)
        layout.addWidget(self.id_field)

        layout.addWidget(self.email_label)
        layout.addWidget(self.email_field)

        layout.addWidget(self.password_label)
        layout.addWidget(self.password_field)

        layout.addWidget(self.register_button)
        layout.addWidget(self.login_button)
        

        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])

    login_dialog = Registro()
    login_dialog.show()

    app.exec()