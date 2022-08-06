import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        button = QPushButton("Vamos!")
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self, checked):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)

# Launch app
app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()

