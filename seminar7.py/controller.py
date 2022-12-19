# Ввод данных данных

from datetime import datetime as dt
from function import*

def greeting():
    print("Добро пожаловать в телефонный справочник!")

def input_data():
    last_name = correct_input("Введите фамилию: ")
    first_name = correct_input("Введите имя: ")
    middle_name = correct_input("Введите отчество: ")

    brith_name = correct_age("Введите год рождения (пример 1950): ")
    phone_number = correct_number("Введите телефонный номер (пример: +74959465735): ")
    note = input("Введите комментарий: ")
    today = dt.now().strftime('%d.%m.%Y - %H:%M')
    return [last_name, first_name, middle_name, brith_name, phone_number, note, today]

