# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'col.ui'
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

class Ui_colwindow(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 322)
        Dialog.setMinimumSize(QSize(800, 322))
        Dialog.setMaximumSize(QSize(800, 322))
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(10, 10, 341, 36))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.colslider = QSlider(Dialog)
        self.colslider.setObjectName(u"colslider")
        self.colslider.setGeometry(QRect(20, 160, 601, 31))
        self.colslider.setMinimum(-180)
        self.colslider.setMaximum(180)
        self.colslider.setPageStep(1)
        self.colslider.setOrientation(Qt.Horizontal)
        self.colvalue = QLabel(Dialog)
        self.colvalue.setObjectName(u"colvalue")
        self.colvalue.setGeometry(QRect(660, 160, 101, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.colvalue.setFont(font1)
        self.colok = QPushButton(Dialog)
        self.colok.setObjectName(u"colok")
        self.colok.setGeometry(QRect(670, 270, 111, 31))

        self.retranslateUi(Dialog)
        self.colslider.valueChanged.connect(self.colvalue.setNum)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Color", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u041e\u0442\u0442\u0435\u043d\u043e\u043a", None))
        self.colvalue.setText(QCoreApplication.translate("Dialog", u"0", None))
        self.colok.setText(QCoreApplication.translate("Dialog", u"OK", None))
    # retranslateUi

