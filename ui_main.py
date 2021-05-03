# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(428, 347)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-20, 0, 501, 381))
        self.frame.setStyleSheet(u"background-color: rgb(46, 52, 54);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(200, 40, 31, 17))
        self.label.setStyleSheet(u"color: rgb(238, 238, 236);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(240, 40, 67, 17))
        self.label_2.setStyleSheet(u"\n"
"color: rgb(204, 0, 0);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(150, 90, 181, 20))
        self.label_3.setStyleSheet(u"font: 75 11pt \"Ubuntu Condensed\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(120, 130, 261, 71))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rb_video = QRadioButton(self.frame_2)
        self.rb_video.setObjectName(u"rb_video")
        self.rb_video.setStyleSheet(u"font: 75 11pt \"Ubuntu Condensed\";\n"
"color: rgb(238, 238, 236);")

        self.horizontalLayout.addWidget(self.rb_video)

        self.rb_audio = QRadioButton(self.frame_2)
        self.rb_audio.setObjectName(u"rb_audio")
        self.rb_audio.setStyleSheet(u"font: 75 11pt \"Ubuntu Condensed\";\n"
"color: rgb(238, 238, 236);")

        self.horizontalLayout.addWidget(self.rb_audio)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(80, 220, 331, 25))
        self.lineEdit.setStyleSheet(u"font: 75 11pt \"Ubuntu Condensed\";")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.btn_dowloand = QPushButton(self.frame)
        self.btn_dowloand.setObjectName(u"btn_dowloand")
        self.btn_dowloand.setGeometry(QRect(200, 270, 89, 25))
        self.btn_dowloand.setStyleSheet(u"font: 75 11pt \"Ubuntu Condensed\";\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"YOU", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"TUBE", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"YouTube Dowloader", None))
        self.rb_video.setText(QCoreApplication.translate("Dialog", u"Video", None))
        self.rb_audio.setText(QCoreApplication.translate("Dialog", u"Audio", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog", u"Link do v\u00eddeo para download", None))
        self.btn_dowloand.setText(QCoreApplication.translate("Dialog", u"BAIXAR", None))
    # retranslateUi

