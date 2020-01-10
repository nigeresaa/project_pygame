import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtWidgets, QtCore


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 1
        label = QLabel(self)
        pixmap = QPixmap('111.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Среднее', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(360, 525)

        self.btn1 = QPushButton('Высшее', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(600, 525)

        self.btn2 = QPushButton('Низшее', self)
        self.btn2.setStyleSheet('background-color: teal;')
        self.btn2.clicked.connect(self.buts2)
        self.btn2.move(130, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="black">В нашем городе открылась новая перспективная компания!</font></b>')
        self.label.move(200, 235)

        self.labe2 = QLabel(self)
        self.labe2.setText(
            '<b><font size="4" color="black">И ты хочешь на неё устроится! Тебя ждут на совещании в 11:00!</font></b>')
        self.labe2.move(200, 245)

        self.labe2 = QLabel(self)
        self.labe2.setText('<b><font size="4" color="black">В отделе кадров тебя спросили:</font></b>')
        self.labe2.move(200, 255)

        self.labe2 = QLabel(self)
        self.labe2.setText('<b><font size="4" color="black">Какое у вас образование?</font></b>')
        self.labe2.move(200, 265)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Лабиринт')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex3 = Example2()

    def buts1(self):
        self.ex3 = Example3()

    def buts2(self):
        self.ex3 = Example30()


class Example2(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 2
        label = QLabel(self)
        pixmap = QPixmap('222.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('ПТУ, я-токарь 3-го разряда', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Строительный по специальности прораб', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(500, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">Что вы закончили и по какой специальности?</font></b>')
        self.label.move(270, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос2')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex4 = Example4()

    def buts1(self):
        self.ex4 = Example5()


class Example3(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 2*
        label = QLabel(self)
        pixmap = QPixmap('222.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Экономическое', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Техническое', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(600, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">Какая у вас специальность?</font></b>')
        self.label.move(350, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос2')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex5 = Example6()

    def buts1(self):
        self.ex5 = Example7()


class Example4(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 3
        label = QLabel(self)
        pixmap = QPixmap('444.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Отлично буду хорошо трудится, делать план', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Это лучше чем ничего', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(500, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Хорошо, у нас есть место для вас в цехе.</font></b>')
        self.label.move(250, 270)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Как ты отнесешься к данной ситуации?</font></b>')
        self.label.move(250, 285)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос3')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex6 = Example8()

    def buts1(self):
        self.ex6 = Example9()


class Example5(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 3*
        label = QLabel(self)
        pixmap = QPixmap('555.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Да, конечно!', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Что еще вы можете предложить?', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(500, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="pink">Отлично есть вакансия мастера в строительном цехе вам это подходит?</font</b>')
        self.label.move(180, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос3')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex6 = Example10()

    def buts1(self):
        self.ex6 = Example11()


class Example6(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 3*%
        label = QLabel(self)
        pixmap = QPixmap('888.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Да, это мне подходит', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('А что еще вы можете мне предложить?', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(500, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="5" color="black">Отлично можем предложить вам должность бухгалтера в фактурном отделе.</font></b>')
        self.label.move(70, 270)

        self.label = QLabel(self)
        self.label.setText("<b>Вас это интересует?</b>")
        self.label.move(200, 280)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос3')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex6 = Example12()

    def buts1(self):
        self.ex6 = Example13()


class Example7(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 3%%
        label = QLabel(self)
        pixmap = QPixmap('555555.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Да, превосходно!', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Нет, я ничего не знаю про AvtoCad', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(500, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="5" color="pink">В настоящее время нам требуется инженер-конструктор.</font></b>')
        self.label.move(200, 100)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Вам это подойдет?</font></b>')
        self.label.move(200, 115)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос3')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex6 = Example14()

    def buts1(self):
        self.ex6 = Example15()


class Example8(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 4
        label = QLabel(self)
        pixmap = QPixmap('666.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Оставлю все как есть, меня все устраивает', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Буду стараться получать 5 разряд', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(500, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="5" color="black">Молодец, ты славно поработал и получил 4 разряд и прибавку к зарплате!</font></b>')
        self.label.move(100, 270)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="black">Что ты будешь делать дальше?</font></b>')
        self.label.move(100, 285)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос4')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex6 = Example16()

    def buts1(self):
        self.ex6 = Example17()


class Example9(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 4
        label = QLabel(self)
        pixmap = QPixmap('66666.png')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Буду искать работу лучше', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Ничего, буду работать кое-как', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(500, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Тебе не очень нравится работать в этой компании.</font</b>')
        self.label.move(200, 270)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Что ты будешь делать дальше?</font></b>')
        self.label.move(200, 285)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос4')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex7 = Example18()

    def buts1(self):
        self.ex7 = Example19()


class Example10(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 4*
        label = QLabel(self)
        pixmap = QPixmap('999.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('С радостью соглашусь', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Не знаю, надо подумать', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(360, 525)

        self.btn2 = QPushButton('Нет, мне и тут хорошо', self)
        self.btn2.setStyleSheet('background-color: teal;')
        self.btn2.clicked.connect(self.buts2)
        self.btn2.move(600, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">Вы отлично справлялись со своими обязанностями</font></b>')
        self.label.move(270, 270)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">и через 4 года вам предложили</font></b>')
        self.label.move(270, 280)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">занять место начальника цеха.</font></b>')
        self.label.move(270, 290)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">Что вы будите делать?</font></b>')
        self.label.move(270, 300)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос4')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex7 = Example20()

    def buts1(self):
        self.ex7 = Example21()

    def buts2(self):
        self.ex7 = Example22()


class Example11(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 4**
        label = QLabel(self)
        pixmap = QPixmap('111111.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Да, конечно!', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Нет, что это?', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(360, 525)

        self.btn2 = QPushButton('Немного', self)
        self.btn2.setStyleSheet('background-color: teal;')
        self.btn2.clicked.connect(self.buts2)
        self.btn2.move(600, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">Вы умеете работать в офисных программах?</font></b>')
        self.label.move(270, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос4')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex7 = Example31()

    def buts1(self):
        self.ex7 = Example32()

    def buts2(self):
        self.ex7 = Example33()


class Example12(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 4*%
        label = QLabel(self)
        pixmap = QPixmap('3333.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Да, очень!', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Нет, это скучно', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(600, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">Вы приступили к работе.</font</b>')
        self.label.move(290, 270)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">Вам нравится новая должность?</font></b>')
        self.label.move(290, 280)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос4')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex7 = Example23()

    def buts1(self):
        self.ex7 = Example24()


class Example13(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 4%%
        label = QLabel(self)
        pixmap = QPixmap('4444.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Я согласен на бухгалтера в фактурном', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(80, 525)

        self.btn1 = QPushButton('Я обдумаю ваше предложение', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(315, 525)

        self.btn2 = QPushButton('Пожалуй я откажусь мне это не подходит', self)
        self.btn2.setStyleSheet('background-color: teal;')
        self.btn2.clicked.connect(self.buts2)
        self.btn2.move(500, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="5" color="black">В данный момент больше вакансий по вашей специальности нет. Так как?</font></b>')
        self.label.move(100, 50)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос4')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex7 = Example25()

    def buts1(self):
        self.ex7 = Example26()

    def buts2(self):
        self.ex7 = Example27()


class Example14(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5
        label = QLabel(self)
        pixmap = QPixmap('666666.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">Вы отлично устроились в этой компании,</font></b>')
        self.label.move(200, 270)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="black">получили новые навыки и нашли более интересное место в соседней компании!</font></b>')
        self.label.move(200, 280)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_18')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example15(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5*
        label = QLabel(self)
        pixmap = QPixmap('777777.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="black">К сожалению мы больше не можем вам ничего предложить!</font></b>')
        self.label.move(230, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_19')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example16(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('777.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец!', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Через 2 года в компании было сокращение.</font></b>')
        self.label.move(200, 90)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Тебя сократили и ты снова очутился на улице.</font></b>')
        self.label.move(200, 105)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_2')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example17(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5*%
        label = QLabel(self)
        pixmap = QPixmap('33333.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Оставлю все как есть, меня устраивает', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.buts)
        self.btn.move(130, 525)

        self.btn1 = QPushButton('Если возможно получу 6 разряд', self)
        self.btn1.setStyleSheet('background-color: red;')
        self.btn1.clicked.connect(self.buts1)
        self.btn1.move(450, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Через 2 года было сокращение,</font></b>')
        self.label.move(200, 270)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="5" color="pink">но тебя повысили дали 5 разряд и оставили работать.</font></b>')
        self.label.move(200, 285)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Что ты будешь делать дальше?</font></b>')
        self.label.move(200, 300)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Вопрос4')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def buts(self):
        self.ex7 = Example28()

    def buts1(self):
        self.ex7 = Example29()


class Example18(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('77777.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example())
        self.btn.move(360, 525)
        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="5" color="pink">Ты нашел место в соседнией компании. Возможно там ты себя проявишь!</font></b>')
        self.label.move(80, 270)
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_5')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example19(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('88888.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Button', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)
        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">В конце концов тебя уволили!</font></b>')
        self.label.move(260, 270)
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_6')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example20(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('1111.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="black">Вы стали отличным начальником цеха,</font></b>')
        self.label.move(270, 270)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="black">доработали до пенсии и много сделали для этой компании!</font></b>')
        self.label.move(270, 280)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_7')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example21(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('99999.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="pink">Пока вы думали место начальника заняли вы остались не у дел!</font></b>')
        self.label.move(200, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_8')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example22(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('2222.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)
        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="black">В компании произошла реорганизация и вашу должность сократили!</font></b>')
        self.label.move(200, 270)
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_9')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example23(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('9999.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="black">Вы закрепились в этой компании и проработали тут до самой пенсии!</font></b>')
        self.label.move(200, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_12')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example24(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('11111.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="black">Вы нашли подходящую должность в соседней компании надеюсь там будет интереснее!</font></b>')
        self.label.move(150, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_13')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example25(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('22222.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="black">Вы поработали в этой компании 3 года.</font></b>')
        self.label.move(150, 270)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="5" color="black">Потом нашли более высокоплачиваемое место в соседней компании!</font></b>')
        self.label.move(150, 285)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_14')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example26(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('5555.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Пока вы думали это место заняли!</font></b>')
        self.label.move(270, 100)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_15')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example27(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('6666.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="5" color="black">Вы нашли очень интересную и высоко оплачиваемую должность в соседней компании!</font></b>')
        self.label.move(10, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_16')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example28(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('44444.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)
        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="5" color="pink">Через 10 лет компания приобрела роботизированный станок и ты стал не нужен!</font></b>')
        self.label.move(50, 270)
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_3')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example29(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('55555.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Через 3 года ты все же получил 6 разряд.</font></b>')
        self.label.move(200, 270)

        self.label = QLabel(self)
        self.label.setText('<b><font size="5" color="pink">Дослужился до пенсии тебе почет и уважение!</font></b>')
        self.label.move(200, 285)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_4')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example30(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('333.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="black">Тебя не взяли на работу из-за не хватки образования!<font></b>')
        self.label.move(230, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_1')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example31(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('222222.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)
        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="pink">Отлично оставте ваш номер телефона мы вам позвони на следующей неделе!</font></b>')
        self.label.move(170, 270)
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_10')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example32(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('333333.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText('<b><font size="4" color="pink">В настоящее время для вас больше ничего нет!</font></b>')
        self.label.move(260, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_11')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


class Example33(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 5**
        label = QLabel(self)
        pixmap = QPixmap('444444.jpg')
        label.setPixmap(pixmap)

        self.btn = QPushButton('Конец', self)
        self.btn.setStyleSheet('background-color: green;')
        self.btn.clicked.connect(self.example)
        self.btn.move(360, 525)

        self.label = QLabel(self)
        self.label.setText(
            '<b><font size="4" color="pink">Оставте свое резюме, возможно мы с вами свяжемся!</font></b>')
        self.label.move(230, 270)

        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Концовка_12')
        self.setWindowIcon(QIcon('web.png'))
        self.show()

    def example(self):
        message = 'Вы уверены, что хотите продолжить?'
        reply = QtWidgets.QMessageBox.question(self, 'Уведомление', message,
                                               QtWidgets.QMessageBox.Yes,
                                               QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            QApplication.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
