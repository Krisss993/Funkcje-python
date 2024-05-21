# Zdefiniuj funkcję o nazwie find_phone_number(), która z przekazanego tekstu wyodrębni numer telefonu w poniższym formacie:
# 123-456-789
# Przykładowe wywołanie funkcji:
# [IN]: find_phone_number('This is my number: 222-456-333.')
# [OUT]: '222-456-333'

import re


def find_phone_number(text):
    pattern = re.compile(r'\b\d{3}-\d{3}-\d{3}\b')
    match = pattern.search(text)
    if match:
        return match.group()
    else:
        return None


# Zdefiniuj funkcję o nazwie union_of_list(), która z przekazanej dowolnej ilości list wyodrębni
# wszystkie unikalne wartości posortowane rosnąco w formie listy (patrz poniżej).

def union_of_list(*data):
    res = []
    for item in data:
        for el in item:
            if el not in res:
                res.append(el)
    return sorted(res)


# Zdefiniuj funkcję o nazwie to_csv(), która z przekazanej dowolnej liczby argumentów
# utworzy ciąg znaków rozdzielony przecinkiem (CSV).
def to_csv(*args):
    res = []
    for i in args:
        res.append(str(i))
    return ','.join(res)

def to_csv(*args):
    return ','.join(str(i) for i in args)

print(to_csv('a','b'))
print(to_csv('a','b'))


# Zdefiniuj funkcję o nazwie to_csv(), która z przekazanej dowolnej liczby argumentów nazwanych
# (keyword arguments) utworzy ciąg znaków rozdzielony przecinkiem (CSV) tak,
# aby nazwy kluczy były nazwami kolumn w formacie CSV (patrz poniżej).


def to_csv(**kwargs):
    names = kwargs.keys()
    val = kwargs.values()
    return ','.join(names) + '\n' + ','.join(str(v) for v in val)



print(to_csv(name='john', age=53, country='USA'))


def validate_point(p):
    if not type(p)==tuple:
        raise TypeError
    if not len(p)==2:
        raise ValueError

print(validate_point((1,1)))
#print(validate_point([1,1]))
print(validate_point(([1,1])))

def validate_point(point):
    if not isinstance(point, (tuple, list)):
        raise TypeError('Point must be a tuple or a list.')
    if not len(point) == 2:
        raise ValueError('Point must consist of two values.')
    for value in point:
        if not isinstance(value, (int, float)):
            raise TypeError('Value must be of type int or float.')
    return True