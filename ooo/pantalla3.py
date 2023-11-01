from PyQt6.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QAction, QVBoxLayout, QLabel, QWidget
 
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
 
        self.setWindowTitle('Paseo Canino')
 
        # Crear el menú
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('Paseador')
 
        # Añadir acciones al menú
        self.map_action = QAction('Mapa', self)
        self.services_action = QAction('Servicios', self)
        self.calendar_action = QAction('Calendario', self)
 
        self.file_menu.addAction(self.map_action)
        self.file_menu.addAction(self.services_action)
        self.file_menu.addAction(self.calendar_action)
 
        # Crear un widget para el contenido principal de la ventana
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
 
        # Crear un layout vertical
        layout = QVBoxLayout()
 
        # Añadir un espacio para el mapa
        self.map_label = QLabel('Aquí se mostrará el mapa.')
        layout.addWidget(self.map_label)
 
        # Aplicar el layout al widget principal
        self.main_widget.setLayout(layout)
 
if __name__ == '__main__':
    app = QApplication([])
 
    main_window = MainWindow()
    main_window.show()
 
    app.exec()