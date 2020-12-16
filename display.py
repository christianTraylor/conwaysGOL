import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import conway

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(qtc.QSize(320, 140))  
        self.setWindowTitle("Conway's Game of Life")
        self.setLayout(qtw.QVBoxLayout())
        self.start()

        self.show()
    
    def start(self):
        self.cells = qtw.QLineEdit()
        #self.cells.text
        startBtn = qtw.QPushButton("Start", self)
        self.layout().addWidget(self.cells)
        self.layout().addWidget(startBtn)
        startBtn.clicked.connect(self.driver)
    
    def driver(self):
        try:
            self.inita = int(self.cells.text())
        except ValueError:
            print("Please enter an integer")
        




app = qtw.QApplication([])
mw = MainWindow()
app.setStyle(qtw.QStyleFactory.create('Fusion'))
app.exec_()