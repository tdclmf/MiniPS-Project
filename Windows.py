import getpass

from PySide6.QtWidgets import QMainWindow, QDialog, QFileDialog
from PySide6.QtCore import Slot, Qt, QEvent
from PySide6.QtGui import QPixmap

from mainw import Ui_MainWindow
from sloywidget import SloiWidget
from bcs import Ui_BCSwindow
from col import Ui_colwindow
from blur import Ui_Blur
from glitch import Ui_glitchwindow


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
        super(MainWindow, self).__init__()
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

    @Slot()
    def addsloywidget(self):
        self.counter_id += 1
        slwidget = SloiWidget(self.counter_id)
        self.ui.SloyWidget_layout.addWidget(slwidget)
        slwidget.delete.connect(self.delete_sloy)

    @Slot(int)
    def delete_sloy(self):
        widget = self.sender()
        self.counter_id -= 1
        self.ui.SloyWidget_layout.removeWidget(widget)
        widget.deleteLater()

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
        if action == self.ui.open:
            fname = QFileDialog.getOpenFileName(self, "Open file", f"c:\\Users\\{getpass.getuser()}\\Desktop.",
                                                "Images (*.jpg *png *jpeg)")
            self.pixmap = QPixmap(fname[0])
            self.im = self.ui.label.setPixmap(self.pixmap)

