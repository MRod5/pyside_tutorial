# Qt Core
from qt_core import *
from gui.pages.ui_pages import Ui_application_pages

# Ventana principal
class UI_MainWindow(object):
    def setup_ui(self, parent):
        # Si la ventana no ha sido editada:
        if not parent.objectName():
            # Cambio del nombre del objeto main window
            parent.setObjectName("MainWindow")

            ## Atributos iniciales
            parent.resize(1600, 900)
            parent.setMinimumSize(960,540)

            # Widget central
            self.central_frame = QFrame()

            # Layout principal
            self.main_layout = QHBoxLayout(self.central_frame)
            self.main_layout.setContentsMargins(0,0,0,0)
            self.main_layout.setSpacing(0)

            ## Contenido
            self.content = QFrame()
            self.content.setStyleSheet("background-color: #282a36")

            # Content Layout
            self.content_layout =QVBoxLayout(self.content)
            self.content_layout.setContentsMargins(0,0,0,0)
            self.content_layout.setSpacing(0)
            
            ## Barra superior
            self.top_bar = QFrame()
            self.top_bar.setMinimumHeight(30)
            self.top_bar.setMaximumHeight(30)
            self.top_bar.setStyleSheet("background-color: #21232d; color:#6272a4")

            self.top_bar_layout = QHBoxLayout(self.top_bar)
            self.top_bar_layout.setContentsMargins(10,0,20,0)

            # Etiqueta izquierda
            self.top_label_left = QLabel("Aplicación de ejemplo con PySide6")

            # Top Spacer
            self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            # Etiqueta derecha
            self.top_label_right = QLabel("| Página Principal")
            self.top_label_right.setStyleSheet("font: 700 9pt 'SegoeUI'")


            ## Páginas de la aplicación
            self.pages = QStackedWidget()
            self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2; background-color: #282a36")
            self.ui_pages = Ui_application_pages()
            self.ui_pages.setupUi(self.pages)
            self.pages.setCurrentWidget(self.ui_pages.page_1)

            ## Barra inferior
            self.bottom_bar = QFrame()
            self.bottom_bar.setMinimumHeight(30)
            self.bottom_bar.setMaximumHeight(30)
            self.bottom_bar.setStyleSheet("background-color: #21232d; color:#6272a4")
            self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
            self.bottom_bar_layout.setContentsMargins(10,0,20,0)

             # Etiqueta izquierda
            self.bottom_bar_label_left = QLabel("MRodriguez")

            # Top Spacer
            self.bottom_bar_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

            # Etiqueta derecha
            self.bottom_bar_label_right = QLabel("2022")
            self.bottom_bar_label_right.setStyleSheet("font: 700 9pt 'SegoeUI'")
           
            #añadir a layout barra superior
            self.bottom_bar_layout.addWidget(self.bottom_bar_label_left)
            self.bottom_bar_layout.addItem(self.bottom_bar_spacer)
            self.bottom_bar_layout.addWidget(self.bottom_bar_label_right)

            #añadir a layout barra superior
            self.top_bar_layout.addWidget(self.top_label_left)
            self.top_bar_layout.addItem(self.top_spacer)
            self.top_bar_layout.addWidget(self.top_label_right)
            

            ## Menú izquierdo
            self.left_menu = QFrame()
            self.left_menu.setStyleSheet("background-color: #44475a")
            self.left_menu.setMaximumWidth(50)
            self.left_menu.setMinimumWidth(50)

            # Left menu layout
            self.left_menu_layout = QVBoxLayout(self.left_menu)
            self.left_menu_layout.setContentsMargins(0,0,0,0)
            self.left_menu_layout.setSpacing(0)

            # Left menu top frame
            self.left_menu_top_frame = QFrame()
            self.left_menu_top_frame.setMinimumHeight(50)
            self.left_menu_top_frame.setObjectName("left_menu_top_frame")
            self.left_menu_top_frame.setStyleSheet("#left_menu_top_frame { background-color: #44475a;}")

            # Left menu top layout
            self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
            self.left_menu_top_layout.setContentsMargins(0,0,0,0)
            self.left_menu_top_layout.setSpacing(0)

            #Top btns izqda
            self.toggle_button = QPushButton("Toggle")
            self.btn1 = QPushButton("1")
            self.btn2 = QPushButton("2")

            # Añade botones a layout izqdo superior
            self.left_menu_top_layout.addWidget(self.toggle_button)
            self.left_menu_top_layout.addWidget(self.btn1)
            self.left_menu_top_layout.addWidget(self.btn2)

            # boton de abajo izqd
            self.botonabajo = QPushButton("Rueda")

            # Left menu bottom frame
            self.left_menu_bottom_frame = QFrame()
            self.left_menu_bottom_frame.setMinimumHeight(50)
            self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
            self.left_menu_bottom_frame.setStyleSheet("#left_menu_bottom_frame {background-color: #44475a; }")
            # Left menu bottom layout
            self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
            self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
            self.left_menu_bottom_layout.setSpacing(0)

            # Añade botones a layout izqdo superior
            self.left_menu_bottom_layout.addWidget(self.botonabajo)

            # Etiqueta menu izqdo abajo
            self.left_menu_label_version = QLabel("version aqui")
            self.left_menu_label_version.setAlignment(Qt.AlignCenter)
            self.left_menu_label_version.setMinimumHeight(30)
            self.left_menu_label_version.setMaximumHeight(30)
            self.left_menu_label_version.setStyleSheet("color: #c3ccdf")

            # Espaciador menu
            self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)

            # Añadir al layout zona izqda
            self.left_menu_layout.addWidget(self.left_menu_top_frame)
            self.left_menu_layout.addItem(self.left_menu_spacer)
            self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
            self.left_menu_layout.addWidget(self.left_menu_label_version)



            ## Añade widgets

            # Widgets en principal
            self.main_layout.addWidget(self.left_menu)
            self.main_layout.addWidget(self.content)

            # Añade widgets en contenido central
            self.content_layout.addWidget(self.top_bar)
            self.content_layout.addWidget(self.pages)
            self.content_layout.addWidget(self.bottom_bar)

            # Widget central:
            parent.setCentralWidget(self.central_frame)


        return None