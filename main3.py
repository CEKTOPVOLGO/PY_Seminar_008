import os
import json

def file_path(file_name='file'):
    return os.path.join(os.path.dirname(__file__), f'{file_name}.txt')



def load_from_file():
    path = file_path()
    with open(path, 'r', encoding='UTF-8') as file:
        data = json.load(file)
    return data




def menu():
    commands = [
        'Показать все контакты',
        'Найти контакт',
        'Создать контакт', 
        'Удалить контакт',
        'Изменить котакт',
        'Выход из программы'
    ]
    print("\n")
    print('Укажите номер команды:')
    print('\n'.join(f'{n}. {v}' for n, v in enumerate(commands, 1)))
    choice = input('>>> ')
    try:
        choice = int(choice)
        if choice < 0 or len(commands) < choice:
            raise Exception('Такой команды пока нет ;(')
        choice -= 1
    except ValueError as ex:
        print('Я вас не понял, повторите...')
        menu()
    except Exception as ex:
        print(ex)
        menu()
    else:
        return choice
    

def show_on_screen(contacts: list) -> None:
    os.system('cls')
    decode_keys = dict(
        first_name='Имя:',
        second_name='Фамилия:',
        contacts='Телефон:'
    )
    pretty_text = str()
    for num, elem in enumerate(contacts, 1):
        pretty_text += f'Контакт №{num}:\n'
        pretty_text += '\n'.join(f'{decode_keys[k]} {v}' for k, v in elem.items())
        pretty_text += '\n________\n'
    print(pretty_text)




def new_contact(contacts: list) -> None:
    # Контактной информации может быть больше чем только телефон
    contacts.append(
        dict(
            first_name=input('Введите имя контакта:\n>>> '),
            second_name=input('Введите фамилию контакта:\n>>> '),
            contacts=input('Введите номер телефона:\n>>> ')
        )
    )



def find_contact(contacts: list) -> dict:
    what = input('Кого ищем?\n>>> ')
    found = list(filter(
        lambda el: what in el['first_name'] or what in el['second_name'], contacts))
    if found:
        show_on_screen(found)
    else:
        print('Никого не нашли ;(')




def save_to_file(contact: list) -> None:
    path = file_path()
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(contact, file, indent = 2, ensure_ascii=False)



def delete_contact(contact: list) -> None:  

    show_on_screen(contact)
    
    choice = input('Номер какого контакта Вы желаете удалить?: ')
    try:
        choice = int(choice)
        if choice < 0 or len(contact) < choice:
            raise Exception('Такой команды пока нет ;(')
        choice -= 1
    except ValueError as ex:
        print('Я вас не понял, повторите...')
        menu()
    except Exception as ex:
        print(ex)
        menu()
    else:
        contact.pop(choice)



def change_contact(contact: list):
    show_on_screen(contact)    
    choice = input('Контакт под каким номером Вы желаете изменить?: ')
    try:
        choice = int(choice)
        if choice < 0 or len(contact) < choice:
            raise Exception('Такой команды пока нет ;(')
        choice -= 1
    except ValueError as ex:
        print('Я вас не понял, повторите...')
        menu()
    except Exception as ex:
        print(ex)
        menu()
    else:
        contact[choice] = dict(
            first_name=input('Введите имя контакта:\n>>> '),
            second_name=input('Введите фамилию контакта:\n>>> '),
            contacts=input('Введите номер телефона:\n>>> ')
        )





def main() -> None:
    print('Программа запущена...')   
    #save_to_file(tests) 
    data = load_from_file()
    flag = True
    while(flag):
        command = menu()
        match command:
            case 0:
                show_on_screen(data)
            case 1:
                find_contact(data)
            case 2:
                new_contact(data)
            case 3:
                delete_contact(data)
            case 4:
                change_contact(data)
            case 5:
                flag = False
        save_to_file(data)
    print('Конец программы!')


if __name__ == '__main__':
    main()