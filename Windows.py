import getpass

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from PIL import Image, ImageFilter, ImageEnhance, ImageQt
from collections import deque
from mainw import Ui_MainWindow
from sloywidget import SloiWidget
from bcs import Ui_BCSwindow
from blur import Ui_Blur
from glitch import Ui_glitchwindow

x = 0
y = 0

class BCSwindow(QDialog):

    def __init__(self, parent):
        super(BCSwindow, self).__init__(parent)
        self.ui = Ui_BCSwindow()
        self.ui.setupUi(self)
        self.ui.bcsok.clicked.connect(self.end)

    def end(self):
        if self.exec_():
            self.val1 = int(self.ui.brightval.text())
            self.val2 = int(self.ui.contval.text())
            self.val3 = int(self.ui.satval.text())
            self.accept()



class Blur(QDialog):

    def __init__(self, parent):
        super(Blur, self).__init__(parent)
        self.ui = Ui_Blur()
        self.ui.setupUi(self)
        self.ui.blurok.clicked.connect(self.end)

    def end(self):
        if self.exec_():
            self.val = int(self.ui.Blurvalue.text())
            self.accept()


class Glitchwindow(QDialog):

    def __init__(self, parent):
        super(Glitchwindow, self).__init__(parent)
        self.ui = Ui_glitchwindow()
        self.ui.setupUi(self)
        self.ui.glitchok.clicked.connect(self.end)


    def end(self):
        if self.exec_():
            self.val = int(self.ui.glitchvalue.text())
            self.accept()

class View(QGraphicsView):

    def mouseMoveEvent(self, event):
        global x
        global y
        x = event.x()
        y = event.y()




class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.counter_id = 0
        self.ui.file.triggered.connect(self.ex)
        self.ui.filter.triggered.connect(self.br)
        self.ui.filter.triggered.connect(self.bl)
        self.ui.eff.triggered.connect(self.glitch)
        self.ui.file.triggered.connect(self.openfile)
        self.ui.holst.triggered.connect(self.on_zoom_in)
        self.ui.holst.triggered.connect(self.on_zoom_out)
        self.ui.sloy.triggered.connect(self.del_cur_layer)
        self.ui.file.triggered.connect(self.save)
        self.layers_pillow = {}
        self.ui.zoomin.setShortcut('Ctrl+=')
        self.ui.zoomout.setShortcut('Ctrl+-')
        self.scene = QGraphicsScene()
        self.canvas = Image.new('RGBA', size = (1000, 1000),
                           color = (255, 255, 255))
        self.layers = {}
        self.canvass = View(self.ui.centralwidget)
        self.canvass.setObjectName(u"canvas")
        self.canvass.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(10)
        sizePolicy2.setVerticalStretch(12)
        sizePolicy2.setHeightForWidth(self.canvass.sizePolicy().hasHeightForWidth())
        self.canvass.setSizePolicy(sizePolicy2)
        self.canvass.setAcceptDrops(False)
        self.canvass.setStyleSheet(u"background-color: rgb(156, 156, 156);")
        self.ui.gridLayout.addWidget(self.canvass, 0, 0, 4, 1)
        self.canvass.setScene(self.scene)
        self.pic = QGraphicsPixmapItem()
        self.scene.addItem(self.pic)
        self.current_layer = None
        self.layers = {}
        self.layers_coord = {}
        self.ui.movelayer.stateChanged.connect(self.ismoveable)

    def rgb_shift(self, im, offset):
        channels = ['r', 'g', 'b']
        image = self.layers_pillow[im]
        image = image.convert('RGB')
        image.load()
        for i in channels:
            r, g, b = image.split()
            eval_getdata = i + ".getdata()"
            channel_data = eval(eval_getdata)
            channel_deque = deque(channel_data)
            channel_deque.rotate(offset)
            eval_putdata = i + ".putdata(channel_deque)"
            eval(eval_putdata)
            image = Image.merge('RGB', (r, g, b))
            offset += 5
        self.layers_pillow[im] = image
        self.update_canvas()

    def blur(self, im, radius):
        image = self.layers_pillow[im]
        image = image.filter(ImageFilter.GaussianBlur(radius=radius * 0.5))
        self.layers_pillow[im] = image
        self.update_canvas()

    def contrast(self, im, factor):
        image = self.layers_pillow[im]
        cont = ImageEnhance.Contrast(image)
        self.layers_pillow[im] = cont.enhance(factor * 0.1)
        self.update_canvas()

    def sat(self, im, factor):
        image = self.layers_pillow[im]
        filter = ImageEnhance.Color(image)
        self.layers_pillow[im] = filter.enhance(factor * 0.1)
        self.update_canvas()

    def brightness(self, im, factor):
        image = self.layers_pillow[im]
        filter = ImageEnhance.Brightness(image)
        self.layers_pillow[im] = filter.enhance(factor * 0.1)
        self.update_canvas()

    @Slot()
    def addsloywidget(self):
        self.counter_id += 1
        slwidget = SloiWidget(self.counter_id)
        self.ui.SloyWidget_layout.addWidget(slwidget)
        self.layers[self.counter_id] = slwidget
        slwidget.delete.connect(self.delete_sloy)
        slwidget.cur.connect(self.curlayer)
        if self.counter_id == 1:
            self.current_layer = slwidget.id_widget
            self.layers[slwidget.id_widget].groupbox.setStyleSheet(u"background-color: rgb(208, 228, 254);")


    @Slot(int)
    def curlayer(self):
        widget = self.sender()
        self.current_layer = widget.current_layer
        print(self.current_layer)
        for i in self.layers:
            if self.layers[i].id_widget != widget.current_layer:
                self.layers[i].groupbox.setStyleSheet(u"background-color: rgb(240, 240, 240);")

    @Slot(int)
    def delete_sloy(self):
        widget = self.sender()
        self.counter_id -= 1
        del self.layers[widget.id_widget]
        del self.layers_pillow[widget.id_widget]
        if self.layers:
            self.current_layer = list(self.layers.keys())[0]
            self.layers[list(self.layers.keys())[0]].groupbox.setStyleSheet(u"background-color: rgb(208, 228, 254);")
        else:
            self.current_layer = None
        self.ui.SloyWidget_layout.removeWidget(widget)
        self.ui.minicanvas.setPixmap(QPixmap())
        self.update_canvas()
        widget.deleteLater()

    def del_cur_layer(self):
        self.ui.SloyWidget_layout.removeWidget(self.layers[self.current_layer])
        del self.layers[self.current_layer]
        del self.layers_pillow[self.current_layer]
        del self.layers_coord[self.current_layer]
        if self.layers:
            self.current_layer = list(self.layers.keys())[0]
        else:
            self.current_layer = None
        self.update_canvas()
        self.layers[self.current_layer].deleteLater()


    @Slot()
    def ex(self, action):
        if action == self.ui.exit:
            self.close()

    def br(self, action):
        if action == self.ui.bright and self.current_layer != None:
            dialog = BCSwindow(self)
            if dialog.exec_() == QDialog.Accepted:
                if dialog.val1 > 0:
                    self.sat(self.current_layer, dialog.val1)
                if dialog.val2 > 0:
                    self.contrast(self.current_layer, dialog.val2)
                if dialog.val3 > 0:
                    self.brightness(self.current_layer, dialog.val3)
            dialog.deleteLater()


    def bl(self, action):
        if action == self.ui.blur and self.current_layer != None:
            dialog = Blur(self)
            if dialog.exec_() == QDialog.Accepted:
                self.blur(self.current_layer, dialog.val)
            else:
                print('Cancelled')
            dialog.deleteLater()

    def glitch(self, action):
        if action == self.ui.glitch and self.current_layer != None:
            dialog = Glitchwindow(self)
            if dialog.exec_() == QDialog.Accepted:
                if dialog.val != 0:
                    self.rgb_shift(self.current_layer, dialog.val)
            else:
                print('Cancelled')
            dialog.deleteLater()

    def openfile(self, action):
        if action == self.ui.open:
            fname = QFileDialog.getOpenFileName(self, "Open file", f"c:\\Users\\{getpass.getuser()}\\Desktop.",
                                                "Images (*.jpg *png *jpeg)")
            if fname[0]:
                self.addsloywidget()
                self.layers_pillow[self.counter_id] = Image.open(fname[0])
                self.layers_coord[self.counter_id] = (0, 0)
                self.update_canvas()
                self.scale_pic = 1

    def ismoveable(self):
        if self.ui.movelayer.isChecked():
            self.canvass.setMouseTracking(True)
        else:
            self.canvass.setMouseTracking(False)

    def mov(self, x, y):
        if self.ui.movelayer.isChecked():
            self.layers_coord[self.current_layer] = (x * 3, y * 3)
            self.update_canvas()

    def mousePressEvent(self, event):
        global x
        global y
        self.mov(x, y)

    def mouseMoveEvent(self, event):
        pass

    def on_zoom_in(self, action):
        if action == self.ui.zoomin:
            self.scale_pic += 0.3
            self.canvass.scale(self.scale_pic, self.scale_pic)
            self.scale_pic = 1

    def on_zoom_out(self, action):
        if action == self.ui.zoomout:
            self.scale_pic -= 0.3
            self.canvass.scale(self.scale_pic, self.scale_pic)
            self.scale_pic = 1

    def update_canvas(self):
        if not self.layers_pillow:
            self.scene.clear()
            self.pic = QGraphicsPixmapItem()
            self.scene.addItem(self.pic)
        else:
            self.new_canvas = self.canvas.copy()
            for key, val in self.layers_pillow.items():
                if key == 1:
                    self.canvas = self.canvas.resize(val.size)
                    self.new_canvas = self.new_canvas.resize(val.size)
                    self.new_canvas.paste(val)
                else:
                    self.new_canvas.paste(val, self.layers_coord[key])
            self.pic.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.new_canvas)))
            self.ui.minicanvas.setPixmap(QPixmap.fromImage(ImageQt.ImageQt(self.new_canvas)).scaledToHeight(self.ui.minicanvas.height()))

    def save(self, action):
        if action == self.ui.save and self.layers:
            sname = QFileDialog.getSaveFileName(self, "Open file", f"c:\\Users\\{getpass.getuser()}\\Desktop.",
                                            "Images (*.jpg *png *jpeg)")
            self.new_canvas.save(sname[0])

