# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bcs.ui'
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

class Ui_BCSwindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 322)
        Dialog.setMinimumSize(QSize(800, 322))
        Dialog.setMaximumSize(QSize(800, 322))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 10, 511, 36))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.satslider = QSlider(Dialog)
        self.satslider.setObjectName(u"satslider")
        self.satslider.setGeometry(QRect(20, 50, 601, 31))
        self.satslider.setMaximum(100)
        self.satslider.setPageStep(1)
        self.satslider.setOrientation(Qt.Horizontal)
        self.brightslider = QSlider(Dialog)
        self.brightslider.setObjectName(u"brightslider")
        self.brightslider.setGeometry(QRect(20, 120, 601, 31))
        self.brightslider.setMaximum(100)
        self.brightslider.setPageStep(1)
        self.brightslider.setOrientation(Qt.Horizontal)
        self.contslider = QSlider(Dialog)
        self.contslider.setObjectName(u"contslider")
        self.contslider.setGeometry(QRect(20, 190, 601, 31))
        self.contslider.setMaximum(50)
        self.contslider.setPageStep(1)
        self.contslider.setOrientation(Qt.Horizontal)
        self.satval = QLabel(Dialog)
        self.satval.setObjectName(u"satval")
        self.satval.setGeometry(QRect(670, 50, 101, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.satval.setFont(font1)
        self.brightval = QLabel(Dialog)
        self.brightval.setObjectName(u"brightval")
        self.brightval.setGeometry(QRect(670, 120, 101, 31))
        self.brightval.setFont(font1)
        self.contval = QLabel(Dialog)
        self.contval.setObjectName(u"contval")
        self.contval.setGeometry(QRect(670, 190, 101, 31))
        self.contval.setFont(font1)
        self.bcsok = QPushButton(Dialog)
        self.bcsok.setObjectName(u"bcsok")
        self.bcsok.setGeometry(QRect(650, 270, 111, 31))

        self.retranslateUi(Dialog)
        self.contslider.valueChanged.connect(self.contval.setNum)
        self.brightslider.valueChanged.connect(self.brightval.setNum)
        self.satslider.valueChanged.connect(self.satval.setNum)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"B/C/S", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u043e\u0441\u0442\u044c/\u042f\u0440\u043a\u043e\u0441\u0442\u044c/\u041a\u043e\u043d\u0442\u0440\u0430\u0441\u0442", None))
        self.satval.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.brightval.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.contval.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.bcsok.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

