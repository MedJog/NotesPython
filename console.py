import text
import datetime
# вызов меню, выбор пунтка меню
def menu()-> int:
    print(text.main_menu)
    while True:
        choise = input(text.menu_choise)
        if choise.isdigit() and 0 < int(choise) < 8:
            return int(choise)
        print(text.input_error) 

# вывод сообщений приложения
def print_message(message: str):
    lenght = len(message)
    print('*' * 50 + '\n')
    print(message)
    print('*' * 50 + '\n')

# создание заметки
def input_note(message : str) -> dict[str, str]:
    print(message)
    title = input(text.new_note[0])
    msg = input(text.new_note[1])
    date = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    return {'title': title, 'msg': msg, 'date': date}
# ввод-вывод
def input_return(message: str) -> str:
    return input(message)

# показать найденные заметки
def show_notes(notes: list[dict[str, str]]):
    if notes:
        print('\n' + '=' * 100)
        for note in notes:
            user_id = note.get('id')
            title = note.get('title')
            msg = note.get('msg')
            date = note.get('date')
            print(f'{user_id:>3}. {title:<10}: {msg:<30}. {date:<10}')
        print('=' * 100 + '\n')
    else:
        print(text.note_not_find)

# показать все заметки
def show_all_notes(notes: list[dict[str, str]]):
    if notes:
        print('\n' + '=' * 100)
        for note in notes:
            user_id = note.get('id')
            title = note.get('title')
            msg = note.get('msg')
            date = note.get('date')
            print(f'{user_id:>3}. {title:<10}: {msg:<30}. {date:<10}')
        print('=' * 100 + '\n')
    else:
        print(text.notes_error)
