import csv 


def overwriting_data(lst):
    new_data = []
    lst+='\n'
    new_data.append(lst)
    with open('phone_book.txt', 'a', encoding='utf-8') as f:
        f.writelines(new_data)


# start_data = [('Иванов Иван Иванович, 123-745\n'), ('Петров Виктор Сергеевич, 983-787\n'), ('Зимина Анна Дмитриевна, 958-114\n')]
# start_data.sort()
# with open('phone_book.txt', 'w', encoding='utf-8') as f:
#     f.writelines(start_data)

def read_data():
    with open('phone_book.txt', 'r', encoding='utf-8') as f:
        contacts = f.read()
    contacts.splitlines()
    contact_list = contacts.split('\n')
    contact_list.remove('')
    contact_list.sort()
    return contact_list

def create_file(reading_data):
    choose_format = input('Укажите требуемый формат: txt или csv ')
    if choose_format == 'txt':
        with open ('user_phone_book.txt', 'w', encoding='utf-8') as f:
            for i in reading_data:
                f.write(i+'\n')
    elif choose_format == 'csv':
        with open ('user_phone_book.csv', mode="w", encoding='utf-8') as f:
            file_writer = csv.writer(f, delimiter = ",", lineterminator="\r")
            file_writer.writerow(reading_data)
    else:
        print('Неизвестный формат')


def user_output_data():
    lst = read_data()
    choose_type = int(input('Если вы хотите вывести информацию на экран, введите 1. Если получить информацию в файле - 0: '))
    if choose_type == 1:
        print(lst)
    elif choose_type == 0:
        create_file(lst)
        
