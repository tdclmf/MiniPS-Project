from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from Widget_Sloi import Ui_Sloi


class SloiWidget(QWidget):
    delete = Signal(int)
    cur = Signal(int)

    def __init__(self, id_widget: int, parent=None):
        super(SloiWidget, self).__init__(parent)
        self.ui = Ui_Sloi()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.label.setText(f"Слой {str(id_widget)}")
        self.ui.deletesloy.clicked.connect(self.press_del)
        self.current_layer = None
        self.groupbox = self.ui.groupBox

    @Slot()
    def mousePressEvent(self, event):
        self.current_layer = self.id_widget
        self.ui.groupBox.setStyleSheet(u"background-color: rgb(208, 228, 254);")
        self.cur.emit(self.current_layer)


    @Slot()
    def press_del(self):
        self.delete.emit(self.id_widget)