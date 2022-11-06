import getpass

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

from mainw import Ui_MainWindow
from sloywidget import SloiWidget
from bcs import Ui_BCSwindow
from col import Ui_colwindow
from blur import Ui_Blur
from glitch import Ui_glitchwindow

files = {}


class BCSwindow(QDialog):

    def __init__(self, parent):
        super(BCSwindow, self).__init__(parent)
        self.ui = Ui_BCSwindow()
        self.ui.setupUi(self)
        self.ui.bcsok.clicked.connect(self.accept)

    @Slot()
    def bcs(self):
        self.close()


class Colwindow(QDialog):

    def __init__(self, parent):
        super(Colwindow, self).__init__(parent)
        self.ui = Ui_colwindow()
        self.ui.setupUi(self)
        self.ui.colok.clicked.connect(self.accept)

    @Slot()
    def color(self):
        self.close()


class Blur(QDialog):

    def __init__(self, parent):
        super(Blur, self).__init__(parent)
        self.ui = Ui_Blur()
        self.ui.setupUi(self)
        self.ui.blurok.clicked.connect(self.accept)

    @Slot()
    def blur(self):
        self.close()


class Glitchwindow(QDialog):

    def __init__(self, parent):
        super(Glitchwindow, self).__init__(parent)
        self.ui = Ui_glitchwindow()
        self.ui.setupUi(self)
        self.ui.glitchok.clicked.connect(self.accept)


class MainWindow(QMainWindow):

    def __init__(self):
        self.pixmaped = 0
        super(MainWindow, self).__init__()
        self.scale = 1
        self.opacity_effect = QGraphicsOpacityEffect()
        self.layer_ids = {}
        self.layer_id = 0
        self.filesid = 0
        self.pixmaps = []
        self.layers = {}
        self.im = None
        self.pixmap = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter_id = 0
        self.ui.addsloy.clicked.connect(self.addsloywidget)
        self.ui.file.triggered.connect(self.ex)
        self.ui.filter.triggered.connect(self.br)
        self.ui.filter.triggered.connect(self.color)
        self.ui.filter.triggered.connect(self.blur)
        self.ui.eff.triggered.connect(self.glitch)
        self.ui.file.triggered.connect(self.openfile)
        self.ui.holst.triggered.connect(self.on_zoom_in)
        self.ui.holst.triggered.connect(self.on_zoom_out)
        self.ui.zoomin.setShortcut('Ctrl+=')
        self.ui.zoomout.setShortcut('Ctrl+-')
        self.ui.addsloy.setEnabled(False)
        self.ui.copy_but.setEnabled(False)
        self.ui.unit.setEnabled(False)

    @Slot()
    def addsloywidget(self):
        self.counter_id += 1
        slwidget = SloiWidget(self.counter_id)
        self.ui.SloyWidget_layout.addWidget(slwidget)
        self.layers[slwidget.id_widget] = QLabel(self.ui.scrollAreaWidgetContents_2)
        self.layers[slwidget.id_widget].setObjectName(u"canvas")
        self.layers[slwidget.id_widget].setSizePolicy(self.ui.sizePolicy4)
        self.layers[slwidget.id_widget].setMaximumSize(QSize(16777215, 16777215))
        self.layers[slwidget.id_widget].setStyleSheet(u"background-color: rgba(0, 0, 0, 0));")
        self.ui.gridLayout_4.addWidget(self.layers[slwidget.id_widget], 0, 0, 1, 1)
        slwidget.delete.connect(self.delete_sloy)

    @Slot(int)
    def delete_sloy(self):
        widget = self.sender()
        if self.counter_id > 1:
            self.counter_id -= 1
            self.ui.SloyWidget_layout.removeWidget(widget)
            self.layers[widget.id_widget].hide()
            del self.pixmaps[widget.id_widget]
            del self.layers[widget.id_widget]
            widget.deleteLater()
        else:
            self.ui.SloyWidget_layout.removeWidget(widget)
            self.counter_id -= 1
            self.ui.addsloy.setEnabled(False)
            self.ui.copy_but.setEnabled(False)
            self.ui.unit.setEnabled(False)
            widget.deleteLater()
            for i in self.layers:
                self.layers[i].clear()

    @Slot()
    def ex(self, action):
        if action == self.ui.exit:
            self.close()

    def br(self, action):
        if action == self.ui.bright:
            dialog = BCSwindow(self)
            if dialog.exec_() == QDialog.Accepted:
                print('accepted')
            else:
                print('Cancelled')
            dialog.deleteLater()

    def color(self, action):
        if action == self.ui.colr:
            dialog = Colwindow(self)
            if dialog.exec_() == QDialog.Accepted:
                print('accepted')
            else:
                print('Cancelled')
            dialog.deleteLater()

    def blur(self, action):
        if action == self.ui.blur:
            dialog = Blur(self)
            if dialog.exec_() == QDialog.Accepted:
                print('accepted')
            else:
                print('Cancelled')
            dialog.deleteLater()

    def glitch(self, action):
        if action == self.ui.glitch:
            dialog = Glitchwindow(self)
            if dialog.exec_() == QDialog.Accepted:
                print('accepted')
            else:
                print('Cancelled')
            dialog.deleteLater()

    def openfile(self, action):
        self.pixmaped += 1
        if action == self.ui.open:
            fname = QFileDialog.getOpenFileName(self, "Open file", f"c:\\Users\\{getpass.getuser()}\\Desktop.",
                                                "Images (*.jpg *png *jpeg)")
            self.addsloywidget()
            self.pixmap = QPixmap(fname[0])
            self.pixmaps.append(self.pixmap)
            self.im = self.layers[-1].setPixmap(self.pixmap)
            self.ui.addsloy.setEnabled(True)
            self.ui.copy_but.setEnabled(True)
            self.ui.unit.setEnabled(True)


    def on_zoom_in(self, action):
        if action == self.ui.zoomin and self.pixmap and self.scale < 6.0:
            self.scale *= 2
            self.resize_image()

    def on_zoom_out(self, action):
        if action == self.ui.zoomout and self.pixmap and self.scale > 0.125:
            self.scale /= 2
            self.resize_image()

    def resize_image(self):
        for i
        size = self.pixmaps[0].size()
        scaled_pixmap = self.pixmaps[0].scaled(self.scale * size)
        self.layers[1].setPixmap(scaled_pixmap)
        self.layers[1].setFixedSize(scaled_pixmap.size())
        self.ui.canvas.setFixedSize(scaled_pixmap.size())

