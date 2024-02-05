import csv,os
from typing import List

def clear_console():
    os.system('clear')

def read_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            return lines
    except FileNotFoundError:
        print('файла нет. Сначала введите данные\n')
        return []

def show_data(data: list):
    for line in data:
        print(line)


def save_data(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        for line in data:
            f.write(line)
    print('изменения зафиксированы')



def search_data(contacts: List[str]):
    # ['Иван, Иванов, Иванович, 123', 'Петр, Иванов, Петрович, 456']
    search_str = input('Введите фамилию для поиска: ')
    founded = []
    # search_idx
    for contact in contacts:
        if search_str.lower() in contact.split(', ')[1].lower():
            founded.append(contact)
    return founded



def edit_line(data, id, file_name):
    print("Что будем изменять 1 - Имя, 2 - Фамилию, 3 - Отчество, 4 - телефон:")
    answer = int(input()) - 1
    print('Введите новые данные')
    pars = data[id].split(', ')
    pars[answer] = input()
    data[id] = ', '.join(pars) + '\n'
    print(['Ошибка редактирования', 'изменения зафиксированы'][save_data(file_name, data)])



def add_data(file):
    print('Введите данные контакта:')
    first_name = input('Введите имя: ')
    last_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    with open(file, 'a', encoding='utf-8') as f:
        f.write(f'{first_name}, {last_name}, {patronymic}, {phone_number}\n')



def main():
    clear_console()
    file_name = 'phone_book.txt'
    if os.path.exists(file_name):
        print ('Найден и загружен телефонный справочник')
        data = read_file(file_name)
    flag = True

    while flag:
        print('0 - выход')
        print('1 - добавить запись в файл')
        print('2 - показать записи')
        print('3 - найти запись')
        print('4 - редактировать запись')
        print('5 - удалить запись')
        answer = input('Выберите действие: ')
        if answer == '0':
            flag = False
        elif answer == '1':
            add_data(file_name)
        elif answer == '2':
            data = read_file(file_name)
            show_data(data)
        elif answer == '3':
            data = read_file(file_name)
            founded_data = search_data(data)
            show_data(founded_data)
        elif answer == '4':
             data = read_file(file_name)
             show_data(data) 
             print ('Введите номер строки для редактирования:') 
             id = int(input())-1
             edit_line(data,id,file_name)
        elif answer == '5': 
             data = read_file(file_name)
             show_data(data) 
             print ('Введите номер строки для удаления:') 
             id = int(input())-1
             del data[id]
             print (['Ошибка удаления','изменения зафиксированы'][save_data(file_name,data)]   )
                               

if __name__ == '__main__':
    main()
