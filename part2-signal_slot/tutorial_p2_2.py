import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        self.label = QLabel()

        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        self.boton = QPushButton("!!!")
        self.boton.clicked.connect(self.limpia)
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.boton)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)

    def limpia(self):
        self.input.setText("Inicializando...")

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()