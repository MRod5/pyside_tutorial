# Qt Core
from qt_core import *

# Ventana principal
class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")

            # Atributos iniciales
            parent.resize(1200, 720)
            parent.setMinimumSize(960,540)

            # Widget central
            self.central_frame = QFrame()

            # Layout principal
            self.main_layout = QHBoxLayout(self.central_frame)
            self.main_layout.setContentsMargins(0,0,0,0)
            self.main_layout.setSpacing(0)

            # Contenido
            self.content = QFrame()
            self.content.setStyleSheet("background-color: #282a36")

            # Menú izquierdo
            self.left_menu = QFrame()
            self.left_menu.setStyleSheet("background-color: #44475a")
            self.left_menu.setMaximumWidth(50)

            # Añade widgets
            self.main_layout.addWidget(self.left_menu)
            self.main_layout.addWidget(self.content)

            # Widget central:
            parent.setCentralWidget(self.central_frame)