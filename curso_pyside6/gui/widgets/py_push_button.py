import os
from qt_core import *

class PyPushButton(QPushButton):
    """
    """

    def __init__(
        self,
        texto="",
        height=40,
        minimum_width=50,
        txt_padding=55,
        text_color="#c3ccdf",
        icon_path="",
        icon_color="#c3ccdf",
        btn_color="#44475a",
        btn_hover="#4f5368",
        btn_pressed="#282a36",
        is_active=False
    ):

        super().__init__()
        return