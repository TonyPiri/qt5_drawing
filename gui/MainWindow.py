from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

from gui.PaintWidget import MyView 



class MainWindow(QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.__initUi()
        self.__initSygnals()
    
    
    def __initUi(self):
        loadUi(r'gui/ui/main_window.ui', self)

        self.paintWidget = MyView()

        self.stackedWidget.addWidget(self.paintWidget)
        self.showPaintWidget()
        
        self.setWindowTitle('Рисовалка Sabai Sabai 2016 ver.0712')
        


##################################################
        self.actionExit.setShortcut('Ctrl+Q')
####################################################



    
    def showPaintWidget(self):
        self.stackedWidget.setCurrentWidget(self.paintWidget)


    def __initSygnals(self):
        self.actionExit.triggered.connect(self.close)
        
