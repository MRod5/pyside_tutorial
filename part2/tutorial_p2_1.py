import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked = True

        self.setWindowTitle("My App")

        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.setChecked(self.button_is_checked)
        self.button.setText("aaaaaah vamos!")
        texto = self.button.text()
        print(texto)
        self.windowTitleChanged.connect(self.titulocambiado)
        self.setCentralWidget(self.button)

    def titulocambiado(self):
        print(" El título cambió!")

    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(checked, self.button.isChecked())

        print(self.button_is_checked)

        self.setWindowTitle("Cambió!")


# Launch app
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

