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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QGroupBox, QLayout, QMainWindow, QMenu,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStatusBar, QVBoxLayout, QWidget)
import res_rc
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1080)
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
        self.gridLayout_2 = QGridLayout(self.derzhalka)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.unit = QPushButton(self.derzhalka)
        self.unit.setObjectName(u"unit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.unit.sizePolicy().hasHeightForWidth())
        self.unit.setSizePolicy(sizePolicy1)
        self.unit.setMinimumSize(QSize(30, 30))
        self.unit.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/res/obed.png", QSize(), QIcon.Normal, QIcon.Off)
        self.unit.setIcon(icon)

        self.gridLayout_2.addWidget(self.unit, 1, 1, 1, 1)

        self.addsloy = QPushButton(self.derzhalka)
        self.addsloy.setObjectName(u"addsloy")
        sizePolicy1.setHeightForWidth(self.addsloy.sizePolicy().hasHeightForWidth())
        self.addsloy.setSizePolicy(sizePolicy1)
        self.addsloy.setMinimumSize(QSize(30, 30))
        self.addsloy.setMaximumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/res/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addsloy.setIcon(icon1)

        self.gridLayout_2.addWidget(self.addsloy, 1, 0, 1, 1)

        self.br_oth = QGroupBox(self.derzhalka)
        self.br_oth.setObjectName(u"br_oth")
        self.br_oth.setMinimumSize(QSize(261, 161))
        self.br_oth.setMaximumSize(QSize(700, 300))

        self.gridLayout_2.addWidget(self.br_oth, 0, 0, 1, 4)

        self.copy_but = QPushButton(self.derzhalka)
        self.copy_but.setObjectName(u"copy_but")
        sizePolicy1.setHeightForWidth(self.copy_but.sizePolicy().hasHeightForWidth())
        self.copy_but.setSizePolicy(sizePolicy1)
        self.copy_but.setMinimumSize(QSize(30, 30))
        self.copy_but.setMaximumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/res/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.copy_but.setIcon(icon2)

        self.gridLayout_2.addWidget(self.copy_but, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.derzhalka, 2, 2, 1, 1)

        self.File = QPushButton(self.centralwidget)
        self.File.setObjectName(u"File")
        sizePolicy1.setHeightForWidth(self.File.sizePolicy().hasHeightForWidth())
        self.File.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.File, 4, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 1, 1, 1)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy2)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 504, 272))
        self.gridLayout_3 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.SloyWidget_layout = QVBoxLayout()
        self.SloyWidget_layout.setObjectName(u"SloyWidget_layout")
        self.SloyWidget_layout.setSizeConstraint(QLayout.SetMaximumSize)

        self.gridLayout_3.addLayout(self.SloyWidget_layout, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 3, 2, 2, 1)

        self.canvas = QGraphicsView(self.centralwidget)
        self.canvas.setObjectName(u"canvas")
        self.canvas.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(10)
        sizePolicy3.setVerticalStretch(12)
        sizePolicy3.setHeightForWidth(self.canvas.sizePolicy().hasHeightForWidth())
        self.canvas.setSizePolicy(sizePolicy3)
        self.canvas.setAcceptDrops(False)
        self.canvas.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.canvas, 0, 0, 4, 1)

        self.Miniholst = QFrame(self.centralwidget)
        self.Miniholst.setObjectName(u"Miniholst")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(4)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.Miniholst.sizePolicy().hasHeightForWidth())
        self.Miniholst.setSizePolicy(sizePolicy4)
        self.Miniholst.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.Miniholst.setFrameShape(QFrame.StyledPanel)
        self.Miniholst.setFrameShadow(QFrame.Raised)

        self.gridLayout.addWidget(self.Miniholst, 0, 2, 2, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1920, 26))
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
        self.st = QMenu(self.menubar)
        self.st.setObjectName(u"st")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.file.menuAction())
        self.menubar.addAction(self.holst.menuAction())
        self.menubar.addAction(self.sloy.menuAction())
        self.menubar.addAction(self.filter.menuAction())
        self.menubar.addAction(self.eff.menuAction())
        self.menubar.addAction(self.st.menuAction())
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
        self.sloy.addAction(self.copy)
        self.sloy.addAction(self.paste)
        self.sloy.addSeparator()
        self.sloy.addAction(self.delmenu)
        self.sloy.addSeparator()
        self.sloy.addAction(self.clear)
        self.filter.addAction(self.col.menuAction())
        self.filter.addAction(self.blur)
        self.col.addAction(self.bright)
        self.col.addAction(self.colr)
        self.eff.addAction(self.glitch)
        self.st.addAction(self.stadd)

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
        self.unit.setText("")
        self.addsloy.setText("")
        self.br_oth.setTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0438\u0441\u0442\u0438", None))
        self.copy_but.setText("")
        self.File.setText(QCoreApplication.translate("MainWindow", u"File 1", None))
        self.file.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b", None))
        self.holst.setTitle(QCoreApplication.translate("MainWindow", u"\u0425\u043e\u043b\u0441\u0442", None))
        self.sloy.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043b\u043e\u0439", None))
        self.filter.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.col.setTitle(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0433\u0443\u043b\u0438\u0440\u043e\u0432\u043a\u0430 \u0446\u0432\u0435\u0442\u0430", None))
        self.eff.setTitle(QCoreApplication.translate("MainWindow", u"\u042d\u0444\u0444\u0435\u043a\u0442\u044b", None))
        self.st.setTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0438\u043a\u0435\u0440\u044b", None))
    # retranslateUi

