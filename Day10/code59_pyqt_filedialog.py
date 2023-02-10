# 다이얼로그
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit(self)
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction('Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('파일열기')
        openFile.triggered.connect(self.onClicked)


        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        # 필수설정
        self.setWindowTitle('파일다이얼로그 위젯')
        self.setGeometry(100, 300, 300, 300)
        # self.showFullScreen() # self.show() # 원래 사이즈
        self.show()

    def onClicked(self):
        fname = QFileDialog.getOpenFileName(self, '파일열기', './')
        
        if fname[0]: # 파일을 선택했다면
            file = open(fname[0], 'rt', encoding='utf-8') # text만 읽겠다
            with file: 
                data = file.read()
                self.textEdit.setText(data)

            file.close()
        
        QMessageBox.about(self, '성공', '로드했습니다.')


    def closeEvent(self, event) -> None: # closeEvent가 생성되어 위젯에 전달된다
        reply = QMessageBox.question(self, '종료', '정말종료하시겠습니까?', 
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept() # 프로그램 종료
        else:
            event.ignore() # 그대로 프로그램 진행...


if __name__ == '__main__':
    app  = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())