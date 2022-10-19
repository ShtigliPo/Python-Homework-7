def get_contact():
    name = input('Имя: ')
    phone = input('Телефон: ')
    return f'{name} || {phone} \n'


def find_contact(book: list, req: str) -> str:
    a = ''
    for i in book:
        if i.find(req) != -1:
            a += f'{i}'
    if a == '':
        return 'Пусто'
    else:
        return a


def get_request():
    return input('Введите имя для поиска контакта: ')


def choose_mode():
    return int(input('Режим записи - 1 ; Режим поиска - 2: '))
