# 다이얼로그
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btnDlg = QPushButton('Dialog', self)
        self.btnDlg.move(20, 20)  # 버튼 위치
        self.btnDlg.clicked.connect(self.onClicked)

        self.txtInput = QLineEdit(self)
        self.txtInput.move(20, 50)

        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        
        # 필수설정
        self.setWindowTitle('이미지 위젯')
        self.setGeometry(100, 300, 300, 300)
        # self.showFullScreen() # self.show() # 원래 사이즈
        self.show()

    def onClicked(self):
        text, ok = QInputDialog.getText(self, '인풋다이얼로그', '이름을 적으세요')
    
        if ok:
            self.txtInput.setText(text)


if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())