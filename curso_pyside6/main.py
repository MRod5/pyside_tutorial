# ## Curso pyside6 por Wanderson Magalhaes
#
# https://github.com/Wanderson-Magalhaes/Curso_PySide6_Em_Portugues
# https://www.youtube.com/watch?v=_qOnJ7-tJcM&list=PLfQ7GQSrl0_ung_Wt0PpgOICqA8k6dr3i

import sys
import os

# Imorta Qt Core
from qt_core import *

from gui.windows.main_window.ui_main_window import *

# Ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Carga de la configuración
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # Visuliza ventana
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())