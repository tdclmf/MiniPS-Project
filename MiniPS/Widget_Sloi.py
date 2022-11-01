# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Widget_Sloi.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_Sloi(object):
    def setupUi(self, Sloi):
        if not Sloi.objectName():
            Sloi.setObjectName(u"Sloi")
        Sloi.resize(582, 72)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Sloi.sizePolicy().hasHeightForWidth())
        Sloi.setSizePolicy(sizePolicy)
        Sloi.setMinimumSize(QSize(0, 0))
        Sloi.setMaximumSize(QSize(16777215, 72))
        self.gridLayout = QGridLayout(Sloi)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox = QGroupBox(Sloi)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QSize(250, 20))
        self.groupBox.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(18)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Symbol"])
        font1.setPointSize(16)
        font1.setBold(False)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.deletesloy = QPushButton(self.groupBox)
        self.deletesloy.setObjectName(u"deletesloy")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.deletesloy.sizePolicy().hasHeightForWidth())
        self.deletesloy.setSizePolicy(sizePolicy2)
        self.deletesloy.setMinimumSize(QSize(30, 30))
        self.deletesloy.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/res/vector-line-black-icon.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.deletesloy.setIcon(icon)
        self.deletesloy.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.deletesloy)


        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)


        self.retranslateUi(Sloi)

        QMetaObject.connectSlotsByName(Sloi)
    # setupUi

    def retranslateUi(self, Sloi):
        Sloi.setWindowTitle(QCoreApplication.translate("Sloi", u"Form", None))
        self.groupBox.setTitle("")
        self.label.setText(QCoreApplication.translate("Sloi", u"\u0421\u043b\u043e\u0439", None))
        self.deletesloy.setText("")
    # retranslateUi

