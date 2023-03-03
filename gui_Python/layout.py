from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class MainWindow (QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Layout")
        self.resize(1280, 720)

        layout = QHBoxLayout()
       
        layout.addWidget(QLabel("stuff 1"))
        layout.addWidget(QLabel("stuff 2"))
        layout.addWidget(QLabel("stuff 3"))
        layout.addWidget(QLabel("stuff 4"))
       
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

  
   
    


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
