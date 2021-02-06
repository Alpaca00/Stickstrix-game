import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize, Qt, QPropertyAnimation, QRect
import style
import random

amount = random.randint(13, 30)
amountChoice = random.randint(1, 50)
count = 0


class StartGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stickstrix')
        self.setWindowIcon(QIcon('icons/matrix.ico'))
        self.setGeometry(570, 250, 250, 250)
        self.setFixedSize(self.size())
        self.setStyleSheet('background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0 #045105, stop: 1 black);')
        self.UI()
        self.moveBox1()
        self.moveBox2()


    def UI(self):
        self.redBtn = QToolButton()
        self.redBtn.setIcon(QIcon('icons/red_pill.png'))
        self.redBtn.setIconSize(QSize(68, 68))
        self.redBtn.setToolTip('Start game')
        self.redBtn.setStyleSheet('border-style: outset; border-width: 2px; border-radius: 8px; border-color: #566573;')
        self.redBtn.move(150, 150)
        self.redBtn.clicked.connect(self.startGame)
        self.blueBtn = QToolButton()
        self.blueBtn.setIcon(QIcon('icons/blue.ico'))
        self.blueBtn.setIconSize(QSize(68, 68))
        self.blueBtn.setToolTip('Exit game')
        self.blueBtn.setStyleSheet('border-style: outset; border-width: 2px; border-radius: 8px; border-color: #566573;')
        self.blueBtn.clicked.connect(self.funcExit)
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.redBtn)
        self.mainLayout.addWidget(self.blueBtn)
        self.setLayout(self.mainLayout)
        self.show()

    def startGame(self):
        self.start = ChoiceGame()
        self.close()

    def funcExit(self):
        self.close()

    def moveBox1(self):
        boxAnimation1 = QPropertyAnimation(self.redBtn, b'geometry')
        boxAnimation1.setDuration(1500)
        boxAnimation1.setStartValue(QRect(0, 0, 0, 0))
        boxAnimation1.setEndValue(QRect(55, 75, 68, 68))
        boxAnimation1.start()
        self.boxAnimation1 = boxAnimation1

    def moveBox2(self):
        boxAnimation2 = QPropertyAnimation(self.blueBtn, b'geometry')
        boxAnimation2.setDuration(1500)
        boxAnimation2.setStartValue(QRect(0, 0, 0, 0))
        boxAnimation2.setEndValue(QRect(130, 75, 68, 68))
        boxAnimation2.start()
        self.boxAnimation2 = boxAnimation2

class ChoiceGame(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stickstrix')
        self.setWindowIcon(QIcon('icons/matrix.ico'))
        self.setGeometry(570, 250, 250, 250)
        self.setFixedSize(self.size())
        self.setStyleSheet('background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0 #045105, stop: 1 black);')
        self.UI()
        self.show()

    def UI(self):
        self.sticksBtn = QToolButton()
        self.sticksBtn.setIcon(QIcon('icons/sticks.png'))
        self.sticksBtn.setIconSize(QSize(68, 68))
        self.sticksBtn.setToolTip('Sticks game')
        self.sticksBtn.setStyleSheet(
                'border-style: outset; border-width: 2px; border-radius: 8px; border-color: #566573;')
        self.sticksBtn.move(150, 150)
        self.sticksBtn.clicked.connect(self.startGameSticks)
        self.choiceBtn = QToolButton()
        self.choiceBtn.setIcon(QIcon('icons/choice.png'))
        self.choiceBtn.setIconSize(QSize(68, 68))
        self.choiceBtn.setToolTip('Choice game')
        self.choiceBtn.setStyleSheet(
                'border-style: outset; border-width: 2px; border-radius: 8px; border-color: #566573;')
        self.choiceBtn.clicked.connect(self.startGameChoice)
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.sticksBtn)
        self.mainLayout.addWidget(self.choiceBtn)
        self.setLayout(self.mainLayout)

    def startGameSticks(self):
        self.start = PlaySticks()
        self.close()

    def startGameChoice(self):
        self.startChoice = PlayChoice()
        self.close()

class PlayChoice(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stickstrix')
        self.setWindowIcon(QIcon('icons/matrix.ico'))
        self.setGeometry(400, 150, 550, 550)
        self.setFixedSize(self.size())
        self.setStyleSheet(style.playgroundStyle())
        self.UI()
        self.show()

    def UI(self):
        self.textGame = QTextEdit()
        self.textGame.setToolTip("""
The computer guesses a number from 1 to 50 and gives 6 attempts to the user to
he was able to guess the hidden number.""")
        self.textGame.setReadOnly(True)
        self.textGame.setStyleSheet(style.textEditStyle())
        self.textGame.setText('How many sticks do you think fell at random?')


        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText('Enter a number')
        self.lineEdit.setStyleSheet(style.lineEditStyle())
        self.confirmBtn = QPushButton('Enter')
        self.confirmBtn.setStyleSheet(style.btnStyle())
        self.confirmBtn.clicked.connect(self.displayGame)
        self.backBtn = QPushButton('Return')
        self.backBtn.setStyleSheet(style.btnStyle())
        self.backBtn.clicked.connect(self.returnBack)

        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topLayout.addWidget(self.textGame)
        self.bottomLayout.addWidget(self.lineEdit)
        self.bottomLayout.addRow(self.backBtn, self.confirmBtn)

        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)


    def displayGame(self):
        global count
        global amountChoice
        numbers = self.lineEdit.text()
        numbers = int(numbers)
        count += 1
        if numbers > amountChoice:
            self.textGame.setText('The number of integers must be no greater than {}'.format(str(numbers)))
            self.lineEdit.setText('')
        elif numbers < amountChoice:
            self.textGame.setText('The number of integers must be greater than {}'.format(str(numbers)))
            self.lineEdit.setText('')
        elif numbers == amountChoice:
            self.textGame.setText('Great you guessed it.\nYou needed was {} attempt.'.format(str(count)))
            self.lineEdit.setText('')
        else:
            self.textGame.setText('Please write a number!')
        if numbers != amountChoice and count > 6:
            self.textGame.setText("You lose!\nPress 'Start' if you want to go again.")

    def returnBack(self):
        self.returnChoiceGame = ChoiceGame()
        self.close()


class PlaySticks(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Stickstrix')
        self.setWindowIcon(QIcon('icons/matrix.ico'))
        self.setGeometry(400, 150, 550, 550)
        self.setFixedSize(self.size())
        self.setStyleSheet(style.playgroundStyle())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        ###widgets of top layout######
        self.textGame = QTextEdit()
        self.textGame.setToolTip("""The game is who takes the last stick is a loser.      
According to the rules, the player must take 1 to 3 sticks. 
A game is starting with a random number.""")
        self.textGame.setReadOnly(True)
        self.textGame.setStyleSheet(style.textEditStyle())
        ###Widgets of bottom layout#####
        self.select1 = QPushButton('1')
        self.select1.setStyleSheet(style.btnStyle())
        self.select1.clicked.connect(self.displayGame)
        self.select2 = QPushButton('2')
        self.select2.setStyleSheet(style.btnStyle())
        self.select2.setCheckable(True)
        self.select2.clicked.connect(self.displayGame)
        self.select3 = QPushButton('3')
        self.select3.setStyleSheet(style.btnStyle())
        self.select3.clicked.connect(self.displayGame)
        self.restartBtn = QPushButton('Start')
        self.restartBtn.clicked.connect(self.runGame)
        self.restartBtn.setStyleSheet(style.btnStyle())
        self.returnBtn = QPushButton('Return')
        self.returnBtn.setStyleSheet(style.btnStyle())
        self.returnBtn.clicked.connect(self.returnMenu)

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QHBoxLayout()
        self.GroupBox = QGroupBox()
        self.GroupBox.setSizePolicy(5,5)
        self.GroupBox.setStyleSheet('border:0px solid #045105;')

        self.topLayout.addWidget(self.textGame)
        self.bottomLayout.setSpacing(5)
        self.bottomLayout.addWidget(self.select1)
        self.bottomLayout.addWidget(self.select2)
        self.bottomLayout.addWidget(self.select3)
        self.bottomLayout.addWidget(self.restartBtn)
        self.bottomLayout.addWidget(self.returnBtn)

        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addWidget(self.GroupBox)
        self.GroupBox.setLayout(self.bottomLayout)
        self.setLayout(self.mainLayout)

    def returnMenu(self):
        self.menuBack = ChoiceGame()
        self.close()

    def runGame(self):
        global amount
        if amount < 31:
            self.textGame.clear()
            amount = random.randint(13, 30)
        self.textGame.append('Welcome to Sticktrix!')
        self.textGame.append('How many sticks do you want to take?\nRandom number to start: {}!'.format(amount))


    def displayGame(self):
        global amount
        sender = self.sender().text()
        sender = int(sender)
        amount -= sender
        self.textGame.append('TAKEN: {}'.format(str(sender)))
        self.textGame.append('REMAINDER: {}'.format(str(amount)))
        taken_max = amount % 4
        if taken_max > 3:
            taken_max = 3
        if taken_max == 0:
            taken_max = 3
        else:
            taken_max -= 1
        if taken_max == 0:
            taken_max = 1
        amount -= taken_max
        self.textGame.append('AI: {}'.format(str(taken_max)))
        self.textGame.append('REMAINDER AFTER AI: {}'.format(str(amount)))
        if amount == 0 or amount < 0:
            self.textGame.append("You win.\nPress 'Start' if you want to go again")
            self.textGame.append('\n')
            amount = random.randint(13, 30)
            self.textGame.append('How many sticks do you want to take?\nRandom number to start: {}!'.format(amount))
        if amount == 1:
            self.textGame.append("YOU LOSE!\nPress 'Start' if you want to go again.")
            self.textGame.append('\n')
            amount = random.randint(13, 30)
            self.textGame.append('How many sticks do you want to take?\nRandom number to start: {}!'.format(amount))


def main():
    app = QApplication(sys.argv)
    window = StartGame()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
