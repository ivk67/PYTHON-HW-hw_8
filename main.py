# import os
# # функция для импорта данных из текстового файла

# def import_data():
#     filename = 'contacts.txt'
#     if os.path.exists(filename):
#         with open(filename, 'r') as f:
#             data = f.readlines()
#         return data
#     else:
#         print('Телефонный справочник не найден')
#         return []
    
# import codecs
# # функция для экспорта данных в текстовый файл
# def export_data(data):
#     with codecs.open('contacts.txt', 'w', encoding='utf-8') as f:
#         f.writelines(data)
#     print('Данные успешно экспортированы')

# # функция для добавления новой записи в справочник
# def add_contact():
#     surname = input('Введите фамилию: ')
#     name = input('Введите имя: ')
#     patronymic = input('Введите отчество: ')
#     phone_number = input('Введите номер телефона: ')
#     new_contact = f'{surname} {name} {patronymic} {phone_number}\n'
#     phone_book.append(new_contact)
#     print('Контакт успешно добавлен')

# # функция для поиска записи в справочнике по фамилии, имени или номеру телефона
# def search_contact():
#     search_query = input('Введите фамилию, имя или номер телефона человека: ')
#     found_contacts = []
#     for contact in phone_book:
#         if search_query in contact:
#             found_contacts.append(contact)
#     if found_contacts:
#         print('Результаты поиска:')
#         for contact in found_contacts:
#             print(contact)
#     else:
#         print('Нет результатов поиска')

# # функция для изменения записи в справочнике
# def edit_contact():
#     search_query = input('Введите фамилию или имя человека для изменения: ')
#     for i, contact in enumerate(phone_book):
#         if search_query in contact:
#             surname, name, patronymic, phone_number = contact.split(' ')
#             new_surname = input(f'Введите новую фамилию (было {surname}): ') or surname
#             new_name = input(f'Введите новое имя (было {name}): ') or name
#             new_patronymic = input(f'Введите новое отчество (было {patronymic}): ') or patronymic
#             new_phone_number = input(f'Введите новый номер телефона (был {phone_number}): ') or phone_number
#             new_contact = f'{new_surname} {new_name} {new_patronymic} {new_phone_number}\n'
#             phone_book[i] = new_contact
#             print('Контакт успешно изменен')
#     else:
#         print('Контакт не найден')

# # функция для удаления записи из справочника
# def delete_contact():
#     search_query = input('Введите фамилию или имя человека для удаления: ')
#     for i, contact in enumerate(phone_book):
#         if search_query in contact:
#             del phone_book[i]
#             print('Контакт успешно удален')
#             break
#     else:
#         print('Контакт не найден')

# # основная функция программы
# def main():
#     global phone_book
#     phone_book = import_data()
#     while True:
#         print('Выберите действие: ')
#         print('1 - Показать всю телефонную книгу')
#         print('2 - Добавить новый контакт')
#         print('3 - Поиск контакта')
#         print('4 - Изменить контакт')
#         print('5 - Удалить контакт')
#         print('0 - Выход')
#         choice = input('Ваш выбор: ')
#         if choice == '1':
#             if phone_book:
#                 print('Телефонная книга: ')
#                 for contact in phone_book:
#                     print(contact)
#             else:
#                 print('Телефонная книга пуста')
#         elif choice == '2':
#             add_contact()
#             export_data(phone_book)
#         elif choice == '3':
#             search_contact()
#         elif choice == '4':
#             edit_contact()
#             export_data(phone_book)
#         elif choice == '5':
#             delete_contact()
#             export_data(phone_book)
#         elif choice == '0':
#             break
#         else:
#             print('Выберите правильный вариант')

# if __name__ == '__main__':
#     main()
############################################################################################################

import os
# функция для импорта данных из текстового файла
def import_data():
    filename = 'contacts.txt'
    if os.path.exists(filename):
        with open(filename, 'r') as f:
            data = f.readlines()
        return data
    else:
        print('Телефонный справочник не найден')
        return []
import codecs
# функция для экспорта данных в текстовый файл
def export_data(data):
    with codecs.open('contacts.txt', 'w', encoding='utf-8') as f:
        f.writelines(data)
    print('Данные успешно экспортированы')

# функция для добавления новой записи в справочник
def add_contact():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone_number = input('Введите номер телефона: ')
    new_contact = f'{last_name} {first_name} {patronymic} {phone_number}\n'
    phone_book.append(new_contact)
    print('Контакт успешно добавлен')

# функция для поиска записи в справочнике по фамилии, имени или номеру телефона
def search_contact():
    search_query = input('Введите фамилию, имя или номер телефона человека: ')
    found_contacts = []
    for contact in phone_book:
        if search_query in contact:
            found_contacts.append(contact)
    if found_contacts:
        print('Результаты поиска:')
        for contact in found_contacts:
            print(contact)
    else:
        print('Нет результатов поиска')

# функция для изменения записи в справочнике
def edit_contact():
    search_query = input('Введите фамилию или имя человека для изменения: ')
    for i, contact in enumerate(phone_book):
        if search_query in contact:
            last_name, first_name, patronymic, phone_number = contact.split(' ')
            new_last_name = input(f'Введите новую фамилию (было {last_name}): ') or last_name
            new_first_name = input(f'Введите новое имя (было {first_name}): ') or first_name
            new_patronymic = input(f'Введите новое отчество (было {patronymic}): ') or patronymic
            new_phone_number = input(f'Введите новый номер телефона (был {phone_number}): ') or phone_number
            new_contact = f'{new_last_name} {new_first_name} {new_patronymic} {new_phone_number}\n'
            phone_book[i] = new_contact
            print('Контакт успешно изменен')
    else:
        print('Контакт не найден')

# функция для удаления записи из справочника
def delete_contact():
    search_query = input('Введите фамилию или имя человека для удаления: ')
    for i, contact in enumerate(phone_book):
        if search_query in contact:
            del phone_book[i]
            print('Контакт успешно удален')
            break
    else:
        print('Контакт не найден')

# основная функция программы
def main():
    global phone_book
    phone_book = import_data()
    while True:
        print('Выберите действие: ')
        print('1 - Показать всю телефонную книгу')
        print('2 - Добавить новый контакт')
        print('3 - Поиск контакта')
        print('4 - Изменить контакт')
        print('5 - Удалить контакт')
        print('0 - Выход')
        choice = input('Ваш выбор: ')
        if choice == '1':
            if phone_book:
                print('Телефонная книга: ')
                for contact in phone_book:
                    print(contact)
            else:
                print('Телефонная книга пуста')
        elif choice == '2':
            add_contact()
            export_data(phone_book)
        elif choice == '3':
            search_contact()
        elif choice == '4':
            edit_contact()
            export_data(phone_book)
        elif choice == '5':
            delete_contact()
            export_data(phone_book)
        elif choice == '0':
            break
        else:
            print('Выберите правильный вариант')

if __name__ == '__main__':
    main()