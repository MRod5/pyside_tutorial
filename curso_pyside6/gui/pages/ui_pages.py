# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagesfTsjnq.ui'
##
## Created by: Qt User Interface Compiler version 6.2.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from qt_core import *

class Ui_application_pages(object):
    def setupUi(self, application_pages):
        if not application_pages.objectName():
            application_pages.setObjectName(u"application_pages")
        application_pages.resize(791, 596)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout = QVBoxLayout(self.page_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        application_pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.page_3)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignBottom|Qt.AlignRight|Qt.AlignTrailing)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        application_pages.addWidget(self.page_3)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.horizontalLayout = QHBoxLayout(self.page_1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.page_1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(500, 70))
        self.frame.setMaximumSize(QSize(500, 70))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 16777210))
        self.label_3.setStyleSheet(u"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.label_3)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(68, 71, 90);\n"
"padding: 8px;\n"
"border: 2px solid #c3ccdf;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.btn_alteraTexto = QPushButton(self.frame)
        self.btn_alteraTexto.setObjectName(u"btn_alteraTexto")
        self.btn_alteraTexto.setMinimumSize(QSize(120, 0))
        self.btn_alteraTexto.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(72, 66, 255);\n"
"padding: 8px;\n"
"border: 2px solid #c3ccdf;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:rgb(85, 170, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color:rgb(255, 0, 127);\n"
"}")

        self.gridLayout_2.addWidget(self.btn_alteraTexto, 0, 1, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)


        self.horizontalLayout.addWidget(self.frame)

        application_pages.addWidget(self.page_1)

        self.retranslateUi(application_pages)

        application_pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(application_pages)
    # setupUi

    def retranslateUi(self, application_pages):
        application_pages.setWindowTitle(QCoreApplication.translate("application_pages", u"StackedWidget", None))
        self.label_2.setText(QCoreApplication.translate("application_pages", u"p2", None))
        self.label.setText(QCoreApplication.translate("application_pages", u"p3", None))
        self.label_3.setText(QCoreApplication.translate("application_pages", u"Hola! :)", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("application_pages", u"Escribe tu nombre", None))
        self.btn_alteraTexto.setText(QCoreApplication.translate("application_pages", u"Altera texto", None))
    # retranslateUi

