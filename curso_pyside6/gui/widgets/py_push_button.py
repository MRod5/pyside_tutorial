import os
from qt_core import *

class PyPushButton(QPushButton):
    """
    """

    def __init__(
        self,
        text="",
        height=50,
        minimum_width=50,
        text_padding=55,
        text_color="#c3ccdf",
        icon_path="",
        icon_color="#c3ccdf",
        btn_color="#44475a",
        btn_hover="#4f5368",
        btn_pressed="#282a36",
        is_active=False
    ):

        super().__init__()

        # Set default parametros
        self.setText(text)
        self.setMaximumHeight(height)
        self.setMinimumHeight(height)
        self.setCursor(Qt.PointingHandCursor)

        # Parametros customizados
        self.minimum_width = minimum_width
        self.text_padding = text_padding
        self.text_color = text_color
        self.icon_path = icon_path
        self.icon_color = icon_color
        self.btn_color = btn_color
        self.btn_hover = btn_hover
        self.btn_pressed = btn_pressed
        self.is_active = is_active

        # Set style
        self.set_style_b(
            text_padding = self.text_padding,
            text_color = self.text_color,
            btn_color = self.btn_color,
            btn_hover = self.btn_hover,
            btn_pressed = self.btn_pressed,
            is_active = self.is_active
            )

        return None

    
    def set_style_b(
        self,
        text_padding = 55,
        text_color = "#c3ccdf",
        btn_color = "#44475a",
        btn_hover = "#4f5368",
        btn_pressed = "#282a36",
        is_active = False
        ):
        style = f"""
        QPushButton {{
            color: {text_color};
            background-color: {btn_color};
            padding-left: {text_padding}px;
            text-align: left;
            border: none;
        }}
        QPushButton:hover {{
            background-color: {btn_hover};
        }}
        QPushButton:pressed {{
            background-color: {btn_pressed};
        }}
        """
        print('--',style)
        self.setStyleSheet(style)

        return None