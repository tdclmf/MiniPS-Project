import getpass

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PIL import Image, ImageFilter, ImageEnhance, ImageQt
from collections import deque
from mainw import Ui_MainWindow
from sloywidget import SloiWidget
from bcs import Ui_BCSwindow
from col import Ui_colwindow
from blur import Ui_Blur
from glitch import Ui_glitchwindow
files = {}


def rgb_shift(image, offset, channel):
    channels = ['r', 'g', 'b']
    for i in channels:
        channels = ['r', 'g', 'b']
        offset = 5
        for i in channels:
            offset += 5
            image = Image.open(image) # заменить
            image = image.convert('RGB')
            image.load()
            r, g, b = image.split()
            eval_getdata = i + ".getdata()"
            channel_data = eval(eval_getdata)
            channel_deque = deque(channel_data)
            channel_deque.rotate(offset)
            eval_putdata = i + ".putdata(channel_deque)"
            eval(eval_putdata)
            image = Image.merge('RGB', (r, g, b))
            # image.save(image) заменить

def blur(image, radius):
    # image = Image.open(image)  заменить
    # image = image.convert('RGB')
    # image.load()
    image.filter(ImageFilter.GaussianBlur(radius=radius))

def contrast(image, factor):
    # image = Image.open(image)  заменить
    # image = image.convert('RGB')
    # image.load()
    filter = ImageEnhance.Contrast(image)
    new_image = image.filter(factor)

def sat(image, factor):
    # image = Image.open(image)  заменить
    # image = image.convert('RGB')
    # image.load()
    filter = ImageEnhance.Color(image)
    new_image = image.filter(factor)

def brightness(image, factor):
    # image = Image.open(image)  заменить
    # image = image.convert('RGB')
    # image.load()
    filter = ImageEnhance.Brightness(image)
    new_image = image.filter(factor)

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
        self.ui.holst.triggered.connect(self.on_zoom_in)
        self.ui.holst.triggered.connect(self.on_zoom_out)
        self.ui.zoomin.setShortcut('Ctrl+=')
        self.ui.zoomout.setShortcut('Ctrl+-')
        self.scene = QGraphicsScene()
        self.ui.addsloy.setEnabled(False)
        self.ui.copy_but.setEnabled(False)
        self.ui.unit.setEnabled(False)
        self.layers = {}
        self.ui.canvas.setScene(self.scene)
        self.current_layer = None

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
        self.scene.removeItem(self.layers[widget.id_widget])
        del self.layers[widget.id_widget]
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
            if fname:
                self.addsloywidget()
                pic = QGraphicsPixmapItem()
                pic.setPixmap(QPixmap(fname[0]))
                if self.counter_id != 1:
                    pic.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable)
                self.layers[self.counter_id] = pic
                self.scene.addItem(self.layers[self.counter_id])
                self.scale_pic = 1


    def on_zoom_in(self, action):
        if action == self.ui.zoomin:
            self.scale_pic += 0.3
            self.ui.canvas.scale(self.scale_pic, self.scale_pic)
            self.scale_pic = 1

    def on_zoom_out(self, action):
        if action == self.ui.zoomout:
            self.scale_pic -= 0.3
            self.ui.canvas.scale(self.scale_pic, self.scale_pic)
            self.scale_pic = 1

