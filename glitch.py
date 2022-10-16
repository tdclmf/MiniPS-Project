# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'glitch.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QSlider, QWidget)

class Ui_glitchwindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 322)
        Dialog.setMinimumSize(QSize(800, 322))
        Dialog.setMaximumSize(QSize(800, 322))
        self.glitchok = QPushButton(Dialog)
        self.glitchok.setObjectName(u"glitchok")
        self.glitchok.setGeometry(QRect(640, 260, 141, 41))
        self.glitchslider = QSlider(Dialog)
        self.glitchslider.setObjectName(u"glitchslider")
        self.glitchslider.setGeometry(QRect(30, 140, 601, 31))
        self.glitchslider.setMaximum(50)
        self.glitchslider.setPageStep(1)
        self.glitchslider.setOrientation(Qt.Horizontal)
        self.glitchvalue = QLabel(Dialog)
        self.glitchvalue.setObjectName(u"glitchvalue")
        self.glitchvalue.setGeometry(QRect(680, 140, 101, 31))
        font = QFont()
        font.setPointSize(12)
        self.glitchvalue.setFont(font)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 30, 371, 36))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.groupBox.setFont(font1)

        self.retranslateUi(Dialog)
        self.glitchslider.valueChanged.connect(self.glitchvalue.setNum)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Glitch", None))
        self.glitchok.setText(QCoreApplication.translate("Dialog", u"\u041e\u041a", None))
        self.glitchvalue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u0422\u043e\u043b\u0449\u0438\u043d\u0430 \u0432\u044b\u0441\u0442\u0443\u043f\u0430 \u0433\u043b\u0438\u0442\u0447\u0430", None))
    # retranslateUi

