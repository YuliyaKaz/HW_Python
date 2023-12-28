# телефонный справочник
from csv import DictReader, DictWriter
from os.path import exists

class lenNumberError(Exception):
    def __init__(self,text):
        self.text = text

def get_info():
    first_name = 'Иван'
    last_name = 'Иванов'
    is_valid_number = False
    while is_valid_number == False:
        try:
            phone_number = int(input('Введите номер: '))
            if len(str(phone_number)) != 3:
                raise lenNumberError('Невалидная длина')
            else:
                is_valid_number = True
        except ValueError:
            print('Невалидный номер')
            continue
        except lenNumberError as err:
            print(err)
            continue
    return[first_name, last_name, phone_number]

def create_file(file_name):
    with open(file_name,'w', encoding='utf-8') as data:
        f_writer = DictWriter(data,fieldnames=["Имя",'Фамилия', 'Телефон'])
        f_writer.writeheader()

def read_file(file_name):
    with open(file_name,'r',encoding='utf-8') as data:
        f_reader = DictReader(data)
        return list(f_reader)

def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    for el in res:
        if el['Телефон'] == str(user_data[2]):
            print('Пользователь уже существует')
            return
    obj = {'Имя': user_data[0],'Фамилия': user_data[1], 'Телефон': user_data[2] }
    res.append(obj)
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Имя','Фамилия', 'Телефон'])
        f_writer.writeheader()
        f_writer.writerows(res)

file_name = 'phone.csv'

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл не создан, создайте его')
                continue
            print(*read_file(file_name))
        elif command == 'c':
            pass


main()
