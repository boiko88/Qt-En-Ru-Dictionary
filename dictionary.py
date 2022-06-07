import csv
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout, QLineEdit
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
from tkcalendar import DateEntry
import random
from css_styles import *


# A Working Sample

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("It's just a test")
window.setFixedWidth(900)
window.setFixedHeight(900)
window.setStyleSheet("background: #7C1FA7")

grid = QGridLayout()

eng_dict = []
rus_dict = []

# Functions 

def test_function():
    print("It actually works")

def add_russian_word():
    actual_new_ru_word = new_rus_entry.text()
    with open ("russian_dictionary.csv", "a", newline="") as data_file:
        data_file.write(f"{actual_new_ru_word}\n")

def add_english_word():
    actual_new_eng_word = new_eng_entry.text()
    with open ("english_dictionary.csv", "a", newline="") as data_file:
        data_file.write(f"{actual_new_eng_word}\n")

def ask_random_eng_word():
    with open ("english_dictionary.csv", "r", newline="") as dictionary:
        eng_dict = dictionary
        actual_dictionary = []
        for line in eng_dict:
            actual_dictionary.append(line)
    print(random.choice(actual_dictionary))


def ask_random_rus_word():
    with open ("russian_dictionary.csv", "r", newline="") as dictionary:
        eng_dict = dictionary
        actual_dictionary = []
        for line in eng_dict:
            actual_dictionary.append(line)
    print(random.choice(actual_dictionary))


        
# Display Dictionary picture
# If you need to cut an Image use - https://photoscissors.com/

image = QPixmap("dictionary_1.png")
dict = QLabel()
dict.setPixmap(image)
dict.setAlignment(QtCore.Qt.AlignCenter)


# Buttons

eng_button = QPushButton("Add english word")
eng_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
eng_button.setStyleSheet(
    beautyful_btn_CSS
    )
eng_button.clicked.connect(add_english_word)

rus_button = QPushButton("Add russian word")
rus_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
rus_button.setStyleSheet(
        beautyful_btn_CSS
    )
rus_button.clicked.connect(add_russian_word)


random_eng_button = QPushButton("Ask Random Eng Word")
random_eng_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
random_eng_button.clicked.connect(ask_random_eng_word)
random_eng_button.setStyleSheet(
    beautyful_btn_CSS
)

random_rus_button = QPushButton("Ask Random Rus Word")
random_rus_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
random_rus_button.clicked.connect(ask_random_rus_word)
random_rus_button.setStyleSheet(
    beautyful_btn_CSS
)


# Entry

new_eng_entry = QLineEdit()
new_eng_entry.setStyleSheet(
        hover_CSS
    )

new_rus_entry = QLineEdit()
new_rus_entry.setStyleSheet(
        hover_CSS
    )

grid.addWidget(eng_button, 0, 0)
grid.addWidget(new_eng_entry, 0,1)

grid.addWidget(rus_button, 1, 0)
grid.addWidget(new_rus_entry, 1,1)

grid.addWidget(random_eng_button, 2, 0)
grid.addWidget(random_rus_button, 2, 1)

window.setLayout(grid)
window.show()
sys.exit(app.exec())
