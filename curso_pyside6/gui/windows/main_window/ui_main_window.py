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
            self.central_frame.setStyleSheet("background-color: #282a36")

            parent.setCentralWidget(self.central_frame)