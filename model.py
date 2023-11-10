from datetime import datetime
from operator import index
import os
notes = []
path = "Notes.csv"

# проверка id
def check_id():
    note_id_list = [0]
    for note in notes:
        note_id_list.append(int(note.get('id')))
    return {'id': str(max(note_id_list) + 1)}

# Добавление новой заметки
def add_new_note(new: dict):
    new.update(check_id())
    notes.append(new)

# поиск Заметки
def search(word: str) -> list[dict]:
    result = []
    for note in notes:
        for key, value in note.items():
            if word.lower() in str(value).lower():
                result.append(note)
                break     
    return result

# поиск индекса в списке
def search_index(index: int):
    for  note in notes:
        if index == int(note.get('id')):
            return notes.index(note)
        
# удаление заметки
def delete_note(index: int):
    print(index)
    del notes[int(index)]

# изменить заметку    
def change(index: int, new: dict[str, str]):
    for key, field in new.items():
        if field != '':
            notes[index][key] = field

# поиск заметки по дате
def search_date(date: str) -> list[dict]:
    result = []
    date = datetime.strptime(date, '%d-%m-%Y')
    date = date.date()
    for note in notes:
        date1 = datetime.strptime(note.get('date'),'%d-%m-%Y %H:%M')
        date1 = date1.date()
        if date == date1:
            result.append(note)
    return result