import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self): 
        super().__init__()
        self.initUI()
        # GUI 화면 설정
        
    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple Window') # 타이틀바 창 제목
        self.setWindowIcon(QIcon('./Day09/iot.png'))
        #self.move(1440 //2 - 200, 900 //2 -200) # 위젯 스크린 이동
        self.resize(400, 200) # 너비, 높이 조정
        self.show() # 핵심 꼭 필요 !! # 스크린에 보여주는 것


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())