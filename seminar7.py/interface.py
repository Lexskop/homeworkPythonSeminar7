from import_export import write_data
from import_export import read_data
from search_data import search_data
from controller import*
from function import print_data

# Часть для ввода команд

def select_operation():
    while True:
        print("Добро пожаловать в телефонный справочник!")
        print('''\nКоманды выбора меню для работы со справочником:
        1 - Добавить контакт 
        2 - Просмотр всех записей
        3 - Поиск контакта
        4 - Удаление контакта
        5 - Изменение контакта
        0 - Выход.\n''')

        menu_selection = input('Введите номер меню: > ')

        if menu_selection == '1':
            list_add=input_data()
            write_data(list_add,sep=",")
        elif menu_selection == '2':
            data = read_data()
            print_data(data)
        elif menu_selection == '3':
            word = input("Введите искомые данные для поиска: ")
            print("Фамилия".center(15), "Имя".center(15), "Отчество".center(15), "Дата рождения".center(15), "Телефон".center(15), "Комментарий".center(20), "Дата и Время внесения".center(20))
            print("-"*125)
            word = word.upper()
            data = read_data()
            for item in search_data(word, data):
                if item != None:
                    print(item[0].center(15), item[1].center(15), item[2].center(15), item[3].center(15), item[4].center(15), item[5].center(20), item[6].center(20))
                else:
                    print("Данные не обнаружены")
        elif menu_selection == '4':    
            # data = add_data()
            a=1
        elif menu_selection == '5':
            # data = add_data()
            a=1    
        elif menu_selection == '0':
            print("Работа завершена")
            raise SystemExit