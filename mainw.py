# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainw.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGraphicsView, QGridLayout, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QScrollArea,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)
import res_rc
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(992, 572)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.open = QAction(MainWindow)
        self.open.setObjectName(u"open")
        self.save = QAction(MainWindow)
        self.save.setObjectName(u"save")
        self.exit = QAction(MainWindow)
        self.exit.setObjectName(u"exit")
        self.otrazhv = QAction(MainWindow)
        self.otrazhv.setObjectName(u"otrazhv")
        self.otrazhg = QAction(MainWindow)
        self.otrazhg.setObjectName(u"otrazhg")
        self.razpo = QAction(MainWindow)
        self.razpo.setObjectName(u"razpo")
        self.razpr = QAction(MainWindow)
        self.razpr.setObjectName(u"razpr")
        self.copy = QAction(MainWindow)
        self.copy.setObjectName(u"copy")
        self.paste = QAction(MainWindow)
        self.paste.setObjectName(u"paste")
        self.delmenu = QAction(MainWindow)
        self.delmenu.setObjectName(u"delmenu")
        self.clear = QAction(MainWindow)
        self.clear.setObjectName(u"clear")
        self.bright = QAction(MainWindow)
        self.bright.setObjectName(u"bright")
        self.colr = QAction(MainWindow)
        self.colr.setObjectName(u"colr")
        self.blur = QAction(MainWindow)
        self.blur.setObjectName(u"blur")
        self.glitch = QAction(MainWindow)
        self.glitch.setObjectName(u"glitch")
        self.stadd = QAction(MainWindow)
        self.stadd.setObjectName(u"stadd")
        self.action_3 = QAction(MainWindow)
        self.action_3.setObjectName(u"action_3")
        self.action_4 = QAction(MainWindow)
        self.action_4.setObjectName(u"action_4")
        self.zoomin = QAction(MainWindow)
        self.zoomin.setObjectName(u"zoomin")
        self.zoomout = QAction(MainWindow)
        self.zoomout.setObjectName(u"zoomout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.derzhalka = QFrame(self.centralwidget)
        self.derzhalka.setObjectName(u"derzhalka")
        self.derzhalka.setFrameShape(QFrame.StyledPanel)
        self.derzhalka.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.derzhalka)
        self.formLayout.setObjectName(u"formLayout")
        self.movelayer = QCheckBox(self.derzhalka)
        self.movelayer.setObjectName(u"movelayer")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.movelayer)


        self.gridLayout.addWidget(self.derzhalka, 2, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy1)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 239, 151))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.SloyWidget_layout = QVBoxLayout()
        self.SloyWidget_layout.setObjectName(u"SloyWidget_layout")
        self.SloyWidget_layout.setSizeConstraint(QLayout.SetMaximumSize)

        self.gridLayout_3.addLayout(self.SloyWidget_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 3, 2, 2, 1)


        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(4)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy3)
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.minicanvas = QLabel(self.frame)
        self.minicanvas.setObjectName(u"minicanvas")
        self.minicanvas.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.minicanvas, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 2, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 992, 26))
        self.file = QMenu(self.menubar)
        self.file.setObjectName(u"file")
        self.holst = QMenu(self.menubar)
        self.holst.setObjectName(u"holst")
        self.sloy = QMenu(self.menubar)
        self.sloy.setObjectName(u"sloy")
        self.filter = QMenu(self.menubar)
        self.filter.setObjectName(u"filter")
        self.col = QMenu(self.filter)
        self.col.setObjectName(u"col")
        self.eff = QMenu(self.menubar)
        self.eff.setObjectName(u"eff")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.holst.menuAction())
        self.menubar.addAction(self.sloy.menuAction())
        self.menubar.addAction(self.filter.menuAction())
        self.menubar.addAction(self.eff.menuAction())
        self.file.addAction(self.open)
        self.file.addSeparator()
        self.file.addAction(self.save)
        self.file.addSeparator()
        self.file.addAction(self.exit)
        self.holst.addAction(self.otrazhv)
        self.holst.addAction(self.otrazhg)
        self.holst.addSeparator()
        self.holst.addAction(self.razpo)
        self.holst.addAction(self.razpr)
        self.holst.addAction(self.zoomin)
        self.holst.addAction(self.zoomout)
        self.sloy.addSeparator()
        self.sloy.addAction(self.delmenu)
        self.sloy.addSeparator()
        self.filter.addAction(self.col.menuAction())
        self.filter.addAction(self.blur)
        self.col.addAction(self.bright)
        self.eff.addAction(self.glitch)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MiniPS", None))
        self.open.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u043a\u0440\u044b\u0442\u044c", None))
        self.save.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.exit.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.otrazhv.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0430\u0437\u0438\u0442\u044c \u0433\u043e\u0440\u0438\u0437\u043e\u043d\u0442\u0430\u043b\u044c\u043d\u043e", None))
        self.otrazhg.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0440\u0430\u0437\u0438\u0442\u044c \u0432\u0435\u0440\u0442\u0438\u043a\u0430\u043b\u044c\u043d\u043e", None))
        self.razpo.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043d\u0430 90\u00b0 \u043f\u043e \u0447\u0430\u0441\u043e\u0432\u043e\u0439", None))
        self.razpr.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0432\u0435\u0440\u043d\u0443\u0442\u044c \u043d\u0430 90\u00b0 \u043f\u0440\u043e\u0442\u0438\u0432 \u0447\u0430\u0441\u043e\u0432\u043e\u0439", None))
        self.copy.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.paste.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0441\u0442\u0430\u0432\u0438\u0442\u044c", None))
        self.delmenu.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c \u0441\u043b\u043e\u0439", None))
        self.bright.setText(QCoreApplication.translate("MainWindow", u"\u042f\u0440\u043a\u043e\u0441\u0442\u044c/\u041d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u043e\u0441\u0442\u044c", None))
        self.colr.setText(QCoreApplication.translate("MainWindow", u"\u0426\u0432\u0435\u0442", None))
        self.blur.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u044b\u0442\u0438\u0435 \u043f\u043e \u0413\u0430\u0443\u0441\u0441\u0443", None))
        self.glitch.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043b\u0438\u0442\u0447 \u044d\u0444\u0444\u0435\u043a\u0442\u044b", None))
        self.stadd.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0441\u0442\u0438\u043a\u0435\u0440", None))
        self.action_3.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u0442\u044c", None))
        self.action_4.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043a\u0430\u043a...", None))
        self.zoomin.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0432\u0435\u043b\u0438\u0447\u0438\u0442\u044c", None))
        self.zoomout.setText(QCoreApplication.translate("MainWindow", u"\u0423\u043c\u0435\u043d\u044c\u0448\u0438\u0442\u044c", None))
        self.movelayer.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u043c\u0435\u0449\u0435\u043d\u0438\u0435 \u0441\u043b\u043e\u044f", None))
        self.minicanvas.setText("")
        self.file.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.holst.setTitle(QCoreApplication.translate("MainWindow", u"\u0425\u043e\u043b\u0441\u0442", None))
        self.sloy.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439", None))
        self.filter.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.col.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u043e\u0432\u043a\u0430 \u0446\u0432\u0435\u0442\u0430", None))
        self.eff.setTitle(QCoreApplication.translate("MainWindow", u"\u042d\u0444\u0444\u0435\u043a\u0442\u044b", None))
    # retranslateUi

