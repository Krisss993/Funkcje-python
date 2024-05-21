# Do ćwiczenia załączony jest plik o nazwie binary.txt zawierający liczby zapisane w systemie binarnym
# (każda liczba to osobna linia):

def binary_to_int():
    with open('binary.txt', 'r') as file:
        text=file.readlines()
        res = [int(x.strip(),2) for x in text]
        return res

print(binary_to_int())


# Zaimplementuj funkcję o nazwie filter_active_users(), która wczyta dołączony plik users.json
# oraz wyciągnie wszystkich aktywnych użytkowników (wartość dla klucza is_active -> true):
# "is_active": true
# Następnie aktywnych użytkowników zrzuć do nowego pliku active_users.json (ustaw poziom wcięcia na 2).
# W rozwiązaniu skorzystaj z pakietu wbudowanego json.

import json

def filter_active_users():
    with open('users.json', 'r') as file:
        content = json.load(file)

    active = [user for user in content if user['is_active']]

    with open('active_users.json', 'w') as output:
        json.dump(active,output, indent=1)

print(filter_active_users())


# Zaimplementuj funkcję o nazwie json_to_csv(), która wczyta dołączony plik users.json,
# przetworzy zawartość pliku na typ csv (comma-separated values) i zapisze do pliku users.csv.
# W rozwiązaniu skorzystaj z pakietu wbudowanego json.

import json

def json_to_csv():
    with open('users.json', 'r') as file:
        content = json.load(file)

    # Transform data
    headers = ','.join(content[0].keys())
    users = [user.values() for user in content]
    rows = [','.join([str(item) for item in user]) for user in users]


        # Load data
    with open('users.csv', 'w') as file:
        file.write(headers + '\n')
        for row in rows:
            file.write(row + '\n')

json_to_csv()




def json_to_csv2():
    with open('users.json', 'r') as file:
        content = json.load(file)
        headers = content[0].keys()
        lines = [[str(item) for item in user.values()] for user in content]

    with open ('users2.csv','w') as output:
        output.write(','.join( str(x) for x in headers)+'\n')
        for line in lines:
            output.write(','.join(str(x) for x in line)+'\n')
json_to_csv2()




# Zaimplementuj funkcję o nazwie json_to_object(), która wczyta dołączony plik users.json.
# Kolejno utworzy klasę User korzystając z modułu wbudowanego collections oraz
# funkcji namedtuple o nazwach atrybutów odpowiadających nazwom kluczy dla każdego użytkownika.
# Następnie dla każdego użytkownika z pliku users.json utwórz instancję klasy User i zwróć
# wszystkich utworzonych użytkowników w formie listy.

from collections import namedtuple


def json_to_object():
    with open('users.json', 'r') as file:
        content = json.load(file)

    attributes = tuple(content[0].keys())

    User = namedtuple('User', attributes)

    values = [tuple(user.values()) for user in content]
    users = [User(*user) for user in values]
    return users

json_to_object()

users = json_to_object()
print(users)

# Zaimplementuj funkcję o nazwie generate_sql(), która przyjmie dwa argumenty:
# table_name - nazwa tabeli (string)
# col_names - nazwy kolumn tabeli (lista, tupla)
#

def generate_sql(table_name, col_names):
    table_n = f'CREATE TABLE {table_name} '
    cols_lst = f'({', '.join(col_names)})'
    return f'{table_n}{cols_lst}'


print(generate_sql('Customer', ['Id', 'FirstName', 'LastName', 'Age']))

def generate_sql(table_name, col_names, constraints):
    table_n = f'CREATE TABLE {table_name} '
    res = ['\n\t'+' '.join((col, const)).strip() for col, const in zip(col_names, constraints)]
    return f"{table_n}({','.join(res)}\n)"


print(generate_sql('Customer', ['Id', 'FirstName'], ['INTEGER PRIMARY KEY', 'TEXT NOT NULL']))
print(generate_sql('Product', ['Id', 'QuantityName'], ['INTEGER PRIMARY KEY', '']))


# Zaimplementuj funkcję o nazwie lev(), która będzie wyznaczać odległość Levenshteina dwóch ciągów znaków.

def lev(a, b):
    if len(b) == 0:
        return len(a)

    if len(a) == 0:
        return len(b)

    if a[0] == b[0]:
        return lev(a[1:], b[1:])

    residual = 1 + min(lev(a[1:], b), lev(a, b[1:]), lev(a[1:], b[1:]))
    return residual


print(lev('hello','legga'))



def get_similar(new):
    words = [
        'friend',
        'friends',
        'friendship',
        'fry',
        'data',
        'database',
        'data science',
        'big data',
        'data cleaning',
        'database',
        'date'
    ]

    scores = []
    for word in words:
        scores.append(lev(new, word))
    res = []
    for w, s in zip(words, scores):
        res.append((w,s))
    s_res = sorted(res, key= lambda x:x[1])
    return s_res[:5]

print(get_similar('big'))
print(get_similar('fri'))

# Przesunięcie powyższego alfabetu o określoną liczbę pozycji, zwaną parametrem przesunięcia
# (w tym przypadku 2) wyznaczy nam szyfr - cipher:

def generate_cipher(alpha, key):

    res = ''
    for i in range(len(alpha)):
        res+=alpha[(i+key)%len(alpha)]
    return res


alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(generate_cipher(alpha, 2))


