# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'blur.ui'
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

class Ui_Blur(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 322)
        Dialog.setMinimumSize(QSize(800, 322))
        Dialog.setMaximumSize(QSize(800, 322))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 10, 341, 36))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.Blurlslider = QSlider(Dialog)
        self.Blurlslider.setObjectName(u"Blurlslider")
        self.Blurlslider.setGeometry(QRect(20, 160, 601, 31))
        self.Blurlslider.setMinimum(0)
        self.Blurlslider.setMaximum(100)
        self.Blurlslider.setPageStep(0)
        self.Blurlslider.setOrientation(Qt.Horizontal)
        self.blurok = QPushButton(Dialog)
        self.blurok.setObjectName(u"blurok")
        self.blurok.setGeometry(QRect(660, 280, 111, 31))
        self.Blurvalue = QLabel(Dialog)
        self.Blurvalue.setObjectName(u"Blurvalue")
        self.Blurvalue.setGeometry(QRect(670, 160, 101, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.Blurvalue.setFont(font1)

        self.retranslateUi(Dialog)
        self.Blurlslider.valueChanged.connect(self.Blurvalue.setNum)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Blur", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u0420\u0430\u0437\u043c\u044b\u0442\u0438\u0435", None))
        self.blurok.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.Blurvalue.setText(QCoreApplication.translate("Dialog", u"0", None))
    # retranslateUi

