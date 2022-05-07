from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QVBoxLayout, QFormLayout, QInputDialog
import json
app = QApplication([])
notes_win = QWidget()
notes = {'Добро пожаловать!':{
    'текст':'В этом приложении можно создать заметки',
    'теги':['умные заметки', 'инструкция']
}}
with open('notes_data.json', 'w') as file:
    json.dump(notes, file)
'''Интерфейс приложения'''
#параметры окна приложения
notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900, 600)

 
#виджеты окна приложения
list_notes = QListWidget()
list_notes_label = QLabel('Список заметок')
 
button_note_create = QPushButton('Создать заметку') #появляется окно с полем "Введите имя заметки"
button_note_del = QPushButton('Удалить заметку')
button_note_save = QPushButton('Сохранить заметку')

button_tag_create = QPushButton('Добавить к заметке') #появляется окно с полем "Введите имя заметки"
button_tag_del = QPushButton('Открепить от заметки')
button_tag_save = QPushButton('Искать заметки по тегу')

def show_note():
    name = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[name]['теги'])
list_notes.itemClicked.connect(show_note)
def add_note():
    note_name, ok = QInputDialog.getText(notes_win, 'Добавить заметку', 'НАзвание заметки:')
    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги' : []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]['теги'])
        print(notes)
button_note_create.clicked.connect(add_note)
def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open ('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        print('Заметка для удаления не выбрана!')
button_note_del.clicked.connect(del_note)
def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open ('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        print('Заметка для сохранения не выбрана!')
def add_tag():
    key = list_notes.selectedItems()[0].text()
    key = field_tag.text()
    if not tag in notes[key]['теги']:
        notes[key]['теги'].appennd(tag)
        list_tags.addItem(tag)
        field_tag.clear()
        with open('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
        print(notes)
    else:
        print('Заметка для добавления тега не выбрана!')

def del_tag():
    if list_tags.selectedItems():
        key = list_notes.selectedItems()[0].text()
        tag = list_tags.selectedItems()[0].text()
        notes[key]['теги'].remove(tag)
        list_tags.clear()
        list_tags.addItems(notes[key]['теги'])
        with open ('notes_data.json', 'w') as file:
            json.dump(notes, file, sort_keys=True)
    else:
        print('Тег для удаления не выбран!')

field_tag = QLineEdit('')
field_tag.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
field_text2 = QTextEdit()
button_tag_add = QPushButton('Добавить к заметке')
button_tag_del = QPushButton('Открепить от заметки')
button_tag_search = QPushButton('Искать заметки по тегу')
list_tags = QListWidget()
list_tags_label = QLabel('Список тегов')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)
 

col_2 = QVBoxLayout()
col_2.addWidget(list_notes_label)
col_2.addWidget(list_notes)

col_2.addWidget(button_note_create)
col_2.addWidget(button_note_del)
col_2.addWidget(button_note_save)
col_2.addWidget(field_tag)
col_2.addWidget(list_tags)
col_2.addWidget(button_tag_create)
col_2.addWidget(button_tag_del)
col_2.addWidget(button_tag_save)

layout_notes.addLayout(col_1, stretch = 2)
layout_notes.addLayout(col_2, stretch = 1)
notes_win.setLayout(layout_notes)
list_notes.addItems(notes)
button_tag_add.clicked.connect(add_tag)
button_tag_del.clicked.connect(del_tag)

button_note_save.clicked.connect(save_note)
notes_win.show()
app.exec_()
