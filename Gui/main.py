import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication, QUrl
import requests
import json
import os


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)
        self.token = QLineEdit("", self)
        self.key = QLineEdit("", self)
        self.name = QLineEdit("", self)
        self.after = QLineEdit("", self)
        self.set_btn = QPushButton('세팅 후 백업 시작')
    
        grid.addWidget(QLabel('토큰 :'), 1, 0)
        grid.addWidget(QLabel('밴드 키 :'), 2, 0)
        grid.addWidget(QLabel('유저 네임 :'), 3, 0)
        grid.addWidget(QLabel('AFTER 값(모를땐 공백) : '),4,0)

        grid.addWidget(self.token ,1,1)
        grid.addWidget(self.key, 2, 1)
        grid.addWidget(self.name, 3, 1)
        grid.addWidget(self.after, 4, 1)
        grid.addWidget(self.set_btn, 5,1)
        self.set_btn.pressed.connect(self.crawl)
        self.setWindowTitle('밴드 백업')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(500, 350)
        self.center()
        self.show()
        announce = QMessageBox()
        announce.setWindowTitle("사용법")
        announce.setText("사용법은 깃허브, 블로그 참고. 프로그램이 꺼지면 작동 끝 혹은 오류입니다.\n자세한 프로그램 사용법은 깃허브 혹은 블로그를 참고하세요\n최대 Quota 무시하는법도 나와있습니다.")
        y = announce.exec_()
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    def crawl(self):
        msg = QMessageBox()
        msg.setWindowTitle("작동중")
        msg.setText("작동중입니다")
        x = msg.exec_()
        token = self.token.text()
        key = self.key.text()
        after = ""
        data = ""
        name = self.name.text()
        URL = 'https://openapi.band.us/v2/band/posts'
        for i in range(0,800):
            if after == "":
                params = {'access_token': token, 'band_key': key}
                response = requests.get(URL, params=params)
                for i in response.json()['result_data']['items']:
                    if i['author']['name']==name:
                        data = i['content']
                        data += "\n\n"
                        with open(os.getcwd() + "/txt/" + i['post_key'] + ".txt", 'w', encoding='utf-8') as f:
                            f.write(data)
                after = response.json()['result_data']['paging']['next_params']['after']
                dataforall+="\n\n\n\n-----------------------------"
            else:
                params = {'access_token': token, 'band_key': key, 'after': after}
                response = requests.get(URL, params=params)
                for i in response.json()['result_data']['items']:
                    if i['author']['name']==name:
                        data = i['content']
                        data += "\n\n"
                        lastjson = response.json()['result_data']['paging']['next_params']['after']
                        with open(os.getcwd() + "/txt/" + i['post_key'] + ".txt", 'w', encoding='utf-8') as f:
                            f.write(data)
                        with open("last"+".json", 'w', encoding='utf-8') as f:
                            f.write(lastjson)
                after = response.json()['result_data']['paging']['next_params']['after']
                print(response.json()['result_data']['paging']['next_params'])
                dataforall += "\n\n\n\n-----------------------------"
        # params = {'access_token': token, 'band_key': key}
        # response = requests.get(URL, params=params)
        # json_str = json.dumps(response.json(), ensure_ascii=False, indent=4)
        # with open("last"+".json", 'w',encoding='utf-8') as f:
        #     f.write(json_str)
        with open("full contents"+".txt", 'w',encoding='utf-8') as f:
            f.write(dataforall)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    app.setWindowIcon(QIcon('icon.png'))
    sys.exit(app.exec_())
    
