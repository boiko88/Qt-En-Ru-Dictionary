import csv
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QWidget, QGridLayout, QLineEdit, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
import random
from css_styles import *
import winsound


# A Working Sample

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("An EN-RU dictionary")
window.setFixedWidth(1100)
window.setFixedHeight(1000)
window.setStyleSheet("background: #7C1FA7")

grid = QGridLayout()

eng_dict = []
rus_dict = []

# Errors

empty_data_error = "Sorry, empty info cannot be added. Please make sure you actually write something before adding it to the dictionary."

# Functions


def add_no_data_error():
    QMessageBox.about(window, "Empty Data Input", empty_data_error)


def add_russian_word():
    actual_new_ru_word = new_rus_entry.text()
    with open("russian_dictionary.csv", "a", newline="") as data_file:
        if actual_new_ru_word == "":
            add_no_data_error()
        else:
            data_file.write(f"{actual_new_ru_word}\n")
            winsound.PlaySound("click.wav", winsound.SND_ASYNC)
            new_rus_entry.clear()


def add_english_word():
    actual_new_eng_word = new_eng_entry.text()
    with open("english_dictionary.csv", "a", newline="") as data_file:
        if actual_new_eng_word == "":
            add_no_data_error()
        else:
            data_file.write(f"{actual_new_eng_word}\n")
            winsound.PlaySound("click.wav", winsound.SND_ASYNC)
            new_eng_entry.clear()


def ask_random_eng_word():
    with open("english_dictionary.csv", "r", encoding='UTF8', newline="") as dictionary:
        eng_dict = dictionary
        actual_dictionary = []
        for line in eng_dict:
            actual_dictionary.append(line)
    revealed_word.setText(f"{random.choice(actual_dictionary)}")
    winsound.PlaySound("click.wav", winsound.SND_ASYNC)


def ask_random_rus_word():
    with open("russian_dictionary.csv", "r", encoding='cp1251', newline="") as dictionary:
        eng_dict = dictionary
        actual_dictionary = []
        for line in eng_dict:
            actual_dictionary.append(line)
    revealed_word.setText(f"{random.choice(actual_dictionary)}")
    winsound.PlaySound("click.wav", winsound.SND_ASYNC)


# Display Pictures

dict_image = QPixmap("dictionary_1.png")
dict = QLabel()
dict.setPixmap(dict_image)
dict.setAlignment(QtCore.Qt.AlignCenter)

english_flag = QPixmap("UK_Flag.png")
uk_flag = QLabel()
uk_flag.setPixmap(english_flag)
uk_flag.setAlignment(QtCore.Qt.AlignCenter)

russian_flag = QPixmap("RU_Flag.png")
ru_flag = QLabel()
ru_flag.setPixmap(russian_flag)
ru_flag.setAlignment(QtCore.Qt.AlignCenter)


# Buttons

eng_button = QPushButton("Add english word")
eng_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
eng_button.setStyleSheet(
    btn_CSS
)
eng_button.clicked.connect(add_english_word)

rus_button = QPushButton("Add russian word")
rus_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
rus_button.setStyleSheet(
    btn_CSS
)
rus_button.clicked.connect(add_russian_word)


random_eng_button = QPushButton("Ask Random Eng Word")
random_eng_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
random_eng_button.clicked.connect(ask_random_eng_word)
random_eng_button.setStyleSheet(
    btn_CSS
)

random_rus_button = QPushButton("Ask Random Rus Word")
random_rus_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
random_rus_button.clicked.connect(ask_random_rus_word)
random_rus_button.setStyleSheet(
    btn_CSS
)


# Entry

new_eng_entry = QLineEdit()
new_eng_entry.setPlaceholderText("Type an English word")
new_eng_entry.setStyleSheet(
    hover_CSS
)

new_rus_entry = QLineEdit()
new_rus_entry.setPlaceholderText("Type a Russia word")
new_rus_entry.setStyleSheet(
    hover_CSS

)

# Label

revealed_word = QLabel()
revealed_word.setStyleSheet(
    label_css_layout
)

# Grid all the elements

grid.addWidget(dict, 0, 0)

grid.addWidget(uk_flag, 1, 0)
grid.addWidget(ru_flag, 1, 1)

grid.addWidget(eng_button, 3, 0)
grid.addWidget(new_eng_entry, 2, 0)

grid.addWidget(rus_button, 3, 1)
grid.addWidget(new_rus_entry, 2, 1)

grid.addWidget(random_eng_button, 4, 0)
grid.addWidget(random_rus_button, 4, 1)

grid.addWidget(revealed_word, 5, 1)


window.setLayout(grid)
window.show()
sys.exit(app.exec())
