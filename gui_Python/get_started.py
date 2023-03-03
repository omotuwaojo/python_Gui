from PyQt5.QtWidgets import *


class MyMainWindow(QMainWindow):
    def __init__(self, *args,  **kwargs):
        super(MyMainWindow, self).__init__( *args,  **kwargs)
        self.setWindowTitle("*introduction to pyq5*")
        self.resize(500, 500)
        label = QLabel("hell ojo what are you ding")
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)
        self.setCentralWidget(label)


app = QApplication([])
window = MyMainWindow()
window.show()
app.exec()