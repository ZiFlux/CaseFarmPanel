from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QDialog
from requests import *
from SimpleQIWI import *
from auth_token import token, phone
import webbrowser
from CasePrices import *
from FAFTUI import *

Form, Window = uic.loadUiType("FAFTUI.ui")
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


class Main(QDialog, Ui_FAFTUI):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)


class Child(QDialog, Ui_CasePrices):
    def __init__(self):
        super(Child, self).__init__()
        self.setupUi(self)

    def OPEN(self):
        self.show()


api = QApi(token=token, phone=phone)
form.networse_2.setText('315')
networse = float(form.networse_2.text())    
percent2 = 5 * 5 / 100
price2 = networse * percent2 / 100
percent1 = 5 + (price2 * 100 / 100)
percent3 = 2
price1 = networse * percent1 / 100
price3 = networse * percent3 / 100
user1 = '@twisttyy'
user2 = '@sashok'
user3 = '@invalid_na...'


def recoil(Ui_CasePrices):
    req1 = requests.get(
        'http://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name=Recoil Case')
    responce1 = req1.json()
    global info1
    info1 = responce1["lowest_price"]
    print(info1)


def fracture():
    req2 = requests.get(
        'http://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name=Fracture Case')
    responce2 = req2.json()
    global info2
    info2 = responce2["lowest_price"]
    print(info2)


def snakebite(self):
    req3 = requests.get(
        'http://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name=Snakebite Case')
    responce3 = req3.json()
    global info3
    info3 = responce3["lowest_price"]
    print(info3)


def DNS():
    req4 = requests.get(
        'http://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name=Dreams%20%26%20Nightmares%20Case')
    responce4 = req4.json()
    global info4
    info4 = responce4["lowest_price"]
    print(info4)


def clutch():
    req5 = requests.get(
        'http://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name=Clutch Case')
    responce5 = req5.json()
    global info5
    info5 = responce5["lowest_price"]
    print(info5)


def prisma2():
    req6 = requests.get(
        'http://steamcommunity.com/market/priceoverview/?appid=730&currency=5&market_hash_name=Prisma 2 Case')
    responce6 = req6.json()
    global info6
    info6 = responce6["lowest_price"]
    print(info6)


def prices22():
    form.label_9.setText(info1)
    form.label_10.setText(info2)
    form.label_10.setText(info3)
    form.label_10.setText(info4)
    form.label_10.setText(info5)
    form.label_10.setText(info6)


def babkivsem():
    api.pay(account="phonenumber", amount=price1, comment='Ваш Доход с фермы!')
    print(price1, 'Отправлены', user1)
    api.pay(account="phonenumber", amount=price2, comment='Ваш Доход с фермы!(@sashok)')
    print(price1, 'Отправлены', user2)
    api.pay(account="phonenumber", amount=price3, comment='Ваш Доход с фермы!')
    print(price1, 'Отправлены', user3)


def babki1():
    api.pay(account="-", amount=price1, comment='Ваш Доход с фермы!')
    print(price1, 'Отправлены', user1)


def babki2():
    api.pay(account="phonenumber", amount=price2, comment='Ваш Доход с фермы!')
    print(price1, 'Отправлены', user2)


def babki3():
    api.pay(account="phonenumber", amount=price3, comment='Ваш Доход с фермы!')
    print(price1, 'Отправлены', user3)


def tg1():
    webbrowser.open('https://t.me/ZiFlux', new=0)


def tg2():
    webbrowser.open('https://t.me/csgofarmbot', new=0)


def tg3():
    webbrowser.open('https://t.me/csgocasefarmbot', new=0)


ch = Child()
form.pushButton.clicked.connect(prices22)
form.PriceButton.clicked.connect(ch.OPEN)
form.pushButton_13.clicked.connect(tg1)
form.pushButton_2.clicked.connect(tg2)
form.pushButton_12.clicked.connect(tg3)
form.client1.clicked.connect(babki1)
form.client2.clicked.connect(babki2)
form.client3.clicked.connect(babki3)
form.PriceButton.clicked.connect(recoil)
form.PriceButton.clicked.connect(fracture)
form.PriceButton.clicked.connect(snakebite)
form.PriceButton.clicked.connect(DNS)
form.PriceButton.clicked.connect(clutch)
form.PriceButton.clicked.connect(prisma2)
app.exec()
