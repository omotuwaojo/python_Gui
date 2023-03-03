from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
         super(MainWindow, self).__init__(*args, **kwargs)
         self.setWindowTitle("Button")
         self.resize(1280, 720)

         layout = QVBoxLayout()

         btn1 = QPushButton('Button 1')
         btn2 = QPushButton('Button 2')
         self.label = QLabel("click button")
         font = self.label.font()
         font.setPointSize(40)
         self.label.setFont(font)
         self.label.setAlignment(Qt.AlignCenter)

         btn1.clicked.connect(self.btn_1_clicked)
         btn2.clicked.connect(self.btn_2_clicked)

         layout.addWidget(self.label)
         layout.addWidget(btn1)
         layout.addWidget(btn2)

         Widget = QWidget()
         Widget.setLayout(layout)
         self.setCentralWidget(Widget)

    def btn_1_clicked(self):
        self.label.setText("Welcome to python GUI(graphic user interface)")

    def btn_2_clicked(self):
        self.label.setText("You clicked botton 2")
        
        

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
