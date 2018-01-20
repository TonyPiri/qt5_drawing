## Рисовалка Sabai Sabai 2016 ver.0712
##
##  All rights reserved
##
## LICENSE: FOR NON-COMERCIAL USE ONLY!

import sys

from PyQt5.QtWidgets import QApplication

from gui.MainWindow import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())
