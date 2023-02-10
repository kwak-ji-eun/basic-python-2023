# 라인에디트 - textbox
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


        
    def initUI(self):
        pixmap = QPixmap('./Day10/cat.png')


        lblImage = QLabel(self)
        lblImage.setPixmap(pixmap)
        lblSize = QLabel(str(pixmap.width()) + 'x' + str(pixmap.height()))
        lblSize.setAlignment(Qt.AlignmentFlag.AlignCenter) # Qt.AlingCenter 가능

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblImage)
        vbox.addWidget(lblSize)
    
        self.setLayout(vbox)

        # 필수설정
        self.setWindowTitle('이미지 위젯')
        self.setGeometry(100, 300, 300, 300)
        # self.showFullScreen()
        self.show() # 원래 사이즈

            # 화면 중심 셋팅
    def setCenter(self):
        qr = self.frameGeometry() # 창 자기자신의 위치값
        cp = QDesktopWidget().availableGeometry().center() # 모니터화면 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onChanged(self, text):
        self.lblResult.setText('입력값: ' + text)
        self.lblResult.adjustSize() # 라벨사이즈 자동


if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())