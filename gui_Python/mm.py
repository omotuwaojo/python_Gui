from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class MainWindow (QMainWindow):
    def __init__(self,*args, **kwargs):
        super(MainWindow, self).__init__(*args,**kwargs)
        self.setWindowTitle("my check box")
        self.resize(100,50)
        layout = QVBoxLayout()

        check1 = QCheckBox("male")
        check2 = QCheckBox("female")
        check3 = QCheckBox("orange")

        layout.addWidget(check1)
        layout.addWidget(check2)
        layout.addWidget(check3)
        widget =QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)




app = QApplication([])
window = MainWindow()
window.show()
app.exec()