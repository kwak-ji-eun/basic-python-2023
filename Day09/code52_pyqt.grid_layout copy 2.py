# 레이아웃 절대적배치

import sys
from PyQt5.QtWidgets import *

class YourApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btnOk = QPushButton('OK')
        btnCancel = QPushButton('Cancel')

        hbox = QHBoxLayout() # hbox = 버튼 두개 옆으로 붙인 것
        hbox.addStretch(1)
        hbox.addWidget(btnOk)
        hbox.addWidget(btnCancel)
        hbox.addStretch(1)
        
        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title'), 0, 0) # row, col = 0, 0
        grid.addWidget(QLabel('Author'), 1, 0)
        grid.addWidget(QLabel('Review'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1) # 0행 1열
        grid.addWidget(QLineEdit(), 1, 1) # 0행 2열
        grid.addWidget(QTextEdit(), 2, 1) # 0행 3열

        btnOk = QPushButton('OK')
        btnCancel = QPushButton('Cancel')

        # 필수 설정
        self.setWindowTitle('박스 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YourApp()
    sys.exit(app.exec_())
    