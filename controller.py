from console import menu,  print_message, input_note, input_return, show_notes, show_all_notes
import text
import model

def start():
    model.open_file()
    #print_message(text.open_successful)
    while True:
        choise = menu()
        match choise:
            case 1:
               # показать все заметки
                show_all_notes(model.notes)
            case 2:
                # создать новую заметку
                new = input_note(text.input_new_note)
                model.add_new_note(new)
                print_message(text.note_saved(new.get('title')))
                show_notes(model.notes)
            case 3:
                # найти заметку
                word = input_return(text.search_word)
                result = model.search(word)
                show_notes(result)
            case 4:
                # изменить заметку
                word = input_return(text.search_word)
                result = model.search(word)
                show_notes(result)
                index = int(input_return(text.input_index))
                new = input_note(text.input_change_note)
                index_in_list = model.search_index(index)
                model.change(index_in_list, new)
                old_note = model.notes[index_in_list].get('title')
                print_message(text.note_changed(new.get('title') if new.get('title') else old_note))
            case 5:
                # удалить заметку
                word = input_return(text.search_word)
                result = model.search(word)
                show_notes(result)
                index = int(input_return(text.input_index_del))
                index_in_list = model.search_index(index)
                model.delete_note(index_in_list)
                print_message(text.note_deleted())
            case 6:
                # поиск заметки по дате
                date = input_return(text.search_date)
                result = model.search_date(date)
                show_notes(result)
            case 7:
                model.save_file(model.notes)
                break
           