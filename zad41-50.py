# Zdefiniuj funkcję o nazwie is_iterable(), która sprawdzi, czy dany obiekt jest iterowalny (iterable).

def is_iterable(obj):
    try:
        iter(obj)
    except TypeError:
        return False
    return True

print(is_iterable(5))
print(is_iterable([5]))


# Zdefiniuj funkcję o nazwie truncate(), która przyjmie dwa argumenty:
# heading - tytuł artykułu w serwisie internetowym
# length - liczba znaków pozostałych po skróceniu tytułu artykułu, domyślnie 30 znaków
# I zwróci skróconą formę tytułu artykułu do 30 znaków, łącznie z trzema kropkami na końcu ... (patrz poniżej):

def truncate(head, length=30):
    if len(head)>length:
        return head[:length-3]+'...'
    return head

print(truncate('Python is a programming language that lets you work quickly.',30))
print(truncate('Python is a programming languag',30))


# Zdefiniuj funkcję o nazwie pascal_traingle(), która przyjmie jeden argument:
# row - numer wiersza w trójkącie Pascala
# I zwróci w formie listy współczynniki odpowiadające podanemu wierszowi trójkąta Pascala.

from math import factorial


def pascal_triangle(row):
    result = []
    for i in range(row + 1):
        factor = factorial(row) // (factorial(i) * factorial(row - i))
        result.append(factor)
    return result



# Załóżmy, że implementujesz pewien proces ETL. Jako dane wejściowe otrzymujesz pliki CSV o następującej strukturze:

# open,high,low,close
# 45.3,46.1,45.3,45.4
# 45.4,46.5,45.0,45.4
# ...

# Zdefiniuj funkcję o nazwie transform(), która będzie przyjmować jeden argument:
# row - jeden wiersz danych z pliku CSV o powyższej postaci (pomijając wiersz z nazwami kolumn)
# i zwracać słownik o poniższej strukturze:
# {'close': 45.4, 'high': 46.1, 'low': 45.3, 'open': 45.3}


def transform(data):
    data=data.split(',')
    dict= {}
    keys = ['open','high','low','close']
    for i,j in zip(keys,data):
        dict[i]=float(j)
    return dict

print(transform('45.3,46.1,45.3,45.4'))


#Podany jest plik app_store.csv dołączony do tego ćwiczenia. Zdefiniuj funkcję o nazwie get_headers(),
# która wczyta podany plik i zwróci w formie listy wszystkie nazwy kolumn z podanego pliku.
# Dokonaj standaryzacji nazw kolumn:
#zamień wszystkie litery na małe
#zamień wszystkie spacje na znaki podkreślenia

def get_headers():
    with open('cs','r') as file:
        headers = file.readline().strip().split(',')
        res = [header.replace(' ','_').lower() for header in headers]
    return res



def preprocess():
    with open('data.csv','r') as file:
        res=[]
        for row in file.readlines():
            r=[]
            for word in row.split(','):
                r.append(word.strip())
            res.append(r)
    return res

print(preprocess())


def calculate_mean_age():
    content = preprocess()
    res = []
    for row in content[1:]:
        res.append(int(row[3]))
    return sum(res) // len(res)

print(calculate_mean_age())

def calculate_mean_age():
    content = preprocess()
    technologies = [x[6] for x in content[1:]]
    count1 = []
    for x in set(technologies):
        count1.append(technologies.count(x))
    res= []
    for x,y in zip(set(technologies), count1):
        res.append((x,y))
    return sorted(res, key=lambda x:x[1], reverse=True)[:3]

print(calculate_mean_age())

from collections import Counter


def top3():
    content = preprocess()
    technologies = [x[6] for x in content[1:]]
    top3=Counter(technologies).most_common(3)
    return top3

print(top3())


# import pandas as pd
# def all_technology():
#     df = pd.read_csv('data.csv')
#     return df['Name'][df['Industry'] == 'Technology'].tolist()
# print(all_technology())


def all_technology():
    content = preprocess()
    res = []
    for row in content:
        if row[6] == 'Technology':
            res.append(row[1])
    return res
print(all_technology())

def all_technology():
    content = preprocess()
    names = [row[1] for row in content[1:] if row[6] == 'Technology']
    return names

print(all_technology())

