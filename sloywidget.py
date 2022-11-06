from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Slot, Signal

from Widget_Sloi import Ui_Sloi


class SloiWidget(QWidget):
    delete = Signal(int)

    def __init__(self, id_widget: int, parent=None):
        super(SloiWidget, self).__init__(parent)
        self.ui = Ui_Sloi()
        self.ui.setupUi(self)
        self.id_widget = id_widget
        self.ui.label.setText(f"Слой {str(id_widget)}")
        self.ui.deletesloy.clicked.connect(self.press_del)

    @Slot()
    def press_del(self):
        self.delete.emit(self.id_widget)