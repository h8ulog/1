from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from random import randint
app=QApplication([])
win=QWidget()
win.setWindowTitle('Лотерея')
win.resize(400,400)
win.move(500,200)
text=QLabel(win)
text.setText("Натисніть щоб взяти участь")
text.move(120,30)

text2=QLabel(win)
text2.setText("?")
text2.move(197,180)

text3=QLabel(win)
text3.setText("?")
text3.move(197,150)

button=QPushButton(win)
button.setText("Випробувати удачу")
button.move(90,250)
button.resize(220,60)

def show_win():
    number=randint(0,9)
    text2.setText(str(number))
    number2=randint(0,9)
    text3.setText(str(number2))
    if number!=number2:
        text.setText("Ви програли! Зіграйте знову")
        text.move(150,30)
    else:
        text.setText("Ви виграли! Зіграйте знову")
        text.move(140,30)
button.clicked.connect(show_win)
win.show()
app.exec()
