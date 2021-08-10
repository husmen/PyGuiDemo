import sys
import random
import cv2 as cv
import PySide6
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        self.suffix = " | PySide ver: {}, QtCore ver: {}".format(PySide6.__version__, QtCore.__version__)

        self.image = cv.imread("D:\\color.tif")
        self.qImage = QtGui.QImage(self.image.data, self.image.shape[1], self.image.shape[0], QtGui.QImage.Format_RGB888).rgbSwapped()
        self.pixmap = QtGui.QPixmap.fromImage(self.qImage).scaled(600, 600, QtCore.Qt.KeepAspectRatio) 
        # or directly from file
        #self.pixmap = QtGui.QPixmap("D:\\color.tif").scaled(600, 600, QtCore.Qt.KeepAspectRatio) 

        self.button = QtWidgets.QPushButton("Click me!")
        self.text = QtWidgets.QLabel("Hello World" + self.suffix, alignment=QtCore.Qt.AlignCenter)
        self.frame = QtWidgets.QLabel()
        self.frame.setPixmap(self.pixmap)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.frame, alignment=QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello) + self.suffix)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())