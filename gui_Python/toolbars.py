from PyQt5.QtWidgets import*
from PyQt5.QtCore import*
from PyQt5.QtGui import*

class MainWindow (QMainWindow):
    def __init__(self,*args,**kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("toolbar")
        self.resize(1280, 720)

        layout = QVBoxLayout()
       
        toolbar = QToolBar("My toolbar")
        action_btn1 = QAction(QIcon(), "paint", self)
        action_btn1.setCheckable(True)
        toolbar.addAction(action_btn1)
        toolbar.addSeparator()
        self.addToolBar(toolbar)
       
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

  
   
    


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
