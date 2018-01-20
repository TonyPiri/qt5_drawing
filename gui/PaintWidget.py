from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView
from PyQt5.QtGui import QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt

from PyQt5.uic import loadUi

#from PyQt5.QtWidgets import QGraphicsSceneMouseEvent 


class MyScene(QGraphicsScene):
    
    def __init__(self):
        super().__init__()
        self.bg = QColor(230,230,230) #цвет бэкграунда и стиралки
        self.lineColor = QColor(0,0,0) #цвет линии поумолчанию
        self.lineSize = 1 #размер по умолчанию

        self.__initUi()

    
    def __initUi(self):
        
        self.setBackgroundBrush(self.bg)
        self.setSceneRect(0,0, 1280,720)
    
        
    def mouseMoveEvent(self, moveEvent):

        self.addLine(moveEvent.lastScenePos().x(),
                     moveEvent.lastScenePos().y(), 
                     moveEvent.scenePos().x(), 
                     moveEvent.scenePos().y(), 
                     QPen(self.lineColor, self.lineSize, Qt.SolidLine, Qt.RoundCap))

    

class MyView(QGraphicsView):
    
    def __init__(self):
        super().__init__()
        self.__initUi()
        self.__initSignals()
  

    def __initUi(self):
        
        loadUi(r'gui/ui/paint_widget.ui', self)
        self.new_scene = MyScene()
        self.graphicsView.setScene(self.new_scene)
        

    def __initSignals(self):
        
        self.sizeSlider.valueChanged.connect(self.sizeValue) 
        
        self.redSlider.valueChanged.connect(self.rgbValue)
        self.greenSlider.valueChanged.connect(self.rgbValue)
        self.blueSlider.valueChanged.connect(self.rgbValue)

        self.brushRadioBtn.pressed.connect(self.rgbValue)
        self.eraserRadioBtn.pressed.connect(self.eraserValues)

        self.clearScenePushBtn.clicked.connect(self.clearScene)
        

    def sizeValue(self):
        self.new_scene.lineSize = self.sizeSlider.value() #слот - размер кисти/стиралки
    
    def rgbValue(self):  
        self.new_scene.lineColor = QColor(self.redSlider.value(), #слот - цвета кисти от значений сладеров 
                                          self.greenSlider.value(), 
                                          self.blueSlider.value())
        
        self.redSlider.setEnabled(True)
        self.greenSlider.setEnabled(True)
        self.blueSlider.setEnabled(True)

    def eraserValues(self):
        self.new_scene.lineColor = self.new_scene.bg #слот - цвет стиралки равный цвету бэкграунда
        
        self.redSlider.setEnabled(False)
        self.greenSlider.setEnabled(False)
        self.blueSlider.setEnabled(False)

    def clearScene(self):
        self.new_scene.clear() #слот очистки сцены
