# Wydrukuj używaną wersję języka Python do konsoli.

import sys

print(sys.version.split(' ')[0])





# Zdefiniuj funkcję o nazwie is_nested(),
# która sprawdzi czy przekazana lista jest zagnieżdżona i składa się z elementów typu list
# (lista składająca się z list).
#[IN]: is_nested([[3, 4]])
#[OUT]: True

def is_nested1(lst):
    if len(lst) == 0:
        return False
    for row in lst:
        if not isinstance(row, list):
            return False
    return True

is_nested1([[1,2]])

def is_nested(arr):
    if len(arr) == 0:
        return False
    return all(isinstance(row, list) for row in arr)





# Zdefiniuj funkcję o nazwie is_all_equal(),
# która sprawdzi czy przekazana lista składa się z tych samych elementów.

def same1(lst):
    c=1
    for i in range(len(lst)-1):
        if lst[i]==lst[i+1]:
            c+=1
    return c==len(lst)

def same(lst):
    return len(set(lst)) == 1

print(same1([1,1,1,1,2]))
print(same1([1,1,1,1,1]))
print(same1([1,1,2,1,1]))
print(same1(['h','h','h']))
print(same1(['a','h','h']))
print()
print(same([1,1,1,1,2]))
print(same([1,1,1,1,1]))
print(same([1,1,2,1,1]))
print(same(['h','h','h']))
print(same(['a','h','h']))





# Podane są dwie zaimplementowane funkcje poniżej:

def is_nested(array):
    if len(array) == 0:
        return False
    return all(isinstance(row, list) for row in array)


def is_all_equal(iterator):
    return len(set(iterator)) <= 1





# Zdefiniuj funkcję o nazwie is_valid_array(),
# która sprawdzi czy z przekazanej listy można zbudować macierz.
# W rozwiązaniu możesz wykorzystać podane funkcje.
# Przekazana lista musi być listą zagnieżdżoną
# oraz każda zagnieżdżona lista powinna składać się z tej samej liczby elementów.

def is_valid_array(arr):
    return is_nested(arr) == True and is_all_equal(len(row) for row in arr) == True

print(is_valid_array([[1,1]]))





# Zdefiniuj funkcję o nazwie swap_elements(),
# która za argument przyjmie listę i zamieni pierwszy i ostatni element tej listy.

def swap_elements(lst):
    lst[0],lst[-1] = lst[-1], lst[0]
    return lst

def swap_elements2(lst):
    temp = lst[0]
    lst[0] = lst[-1]
    lst[-1] = temp
    return lst





# Zdefiniuj funkcję o nazwie swap_elements(),
# która za argument przyjmie listę oraz dwa indeksy i zamieni elementy na wskazanych indeksach.

def swap_elements3(lst, i, j):
    lst[i],lst[j] = lst[j], lst[i]
    return lst

def swap_elements4(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp
    return lst





# Zdefiniuj funkcję o nazwie reverse_words(),
# która za argument przyjmie tekst i odwróci kolejność słów w podanym tekście.
# Dla uproszczenia zakładamy, że tekst nie zawiera żadnych znaków interpunkcyjnych.

def reverse_words(words):
    return ' '.join(words.split()[::-1])

print(reverse_words('Hello there you'))





# Zdefiniuj funkcję o nazwie remove_common_elements(),
# która za argument przyjmie dwie listy,
# usunie ich wspólne elementy i zwróci te listy.

def remove_common_elements(lst1, lst2):
    l1 = [x for x in lst1 if x not in lst2]
    l2 = [x for x in lst2 if x not in lst1]
    return l1, l2

print(remove_common_elements([0,1,2,3,4],[5,4,3,2,1]))





# Zdefiniuj funkcję o nazwie get_indices(),
# która za argument przyjmie listę oraz szukany element i
# zwróci listę wszystkich indeksów na których znajduje się szukany element.
# Jeśli element nie występuje w liście funkcja zwraca pustą listę.

def get_indices(lst, el):
    res = []
    for i in range(len(lst)):
        if lst[i] == el:
            res.append(i)
    return res

def get_indices2(lst, el):
    res = []
    for i, val in enumerate(lst):
        if val == el:
            res.append(i)
    return res

print(get_indices2([1,1,2,3,5,7,2],2))




# Zdefiniuj funkcję o nazwie get_indices(),
# która za argument przyjmie listę oraz zwróci listę wszystkich indeksów
# na których znajduje się element typu str.
# Jeśli lista nie posiada żadnych elementów typu str funkcja ma zwrócić pustą listę.


def get_indices(lst):
    res = []
    for i, el in enumerate(lst):
        if isinstance(el, str):
            res.append(i)
    return res

def get_indices2(lst):
    res = []
    for i in range(len(lst)):
        if isinstance(lst[i], str):
            res.append(i)
    return res

print(get_indices(['Hello','There',2]))
print(get_indices2(['Hello','There',2]))


# Zdefiniuj funkcję o nazwie convert(),
# która za argument przyjmie listę słowników poniższej postaci:
data = [
    {'user': 'joe', 'main_technology': 'python'},
    {'user': 'tom', 'main_technology': 'c/cpp'},
    {'user': 'michael', 'main_technology': 'cloud'},
    {'user': 'bob', 'main_technology': 'php'},
    {'user': 'lil', 'main_technology': 'html'},
    {'user': 'alice', 'main_technology': 'sql'},
]
# I zwróci słownik grupujący elementy po kluczach słownika do list (patrz poniżej).


def convert(dta):
    res= {}
    keys = dta[0].keys()
    print(keys)
    for key in keys:
        if key not in res.keys():
            res[key] = []
    for val in dta:
        for k in keys:
            res[k].append(val[k])
    return res

print(convert(data))

def convert(data):
    res = {}
    for row in data:
        for key, value in row.items():
            if key not in res.keys():
                res[key] = []
            res[key].append(value)
    return res

print(convert(data))







data = [
    {'user': 'joe', 'main_technology': 'python'},
    {'user': 'tom', 'main_technology': 'c/cpp'},
    {'user': 'michael', 'main_technology': 'cloud'},
    {'user': 'bob', 'main_technology': 'php'},
    {'user': 'lil', 'main_technology': 'html'},
    {'user': 'alice', 'main_technology': 'sql'},
]

def func(data):
    res = {}
    for dict in data:
        for k,v in dict.items():
            if k not in res.keys():
                res[k] = []
            res[k].append(v)

    return res


print()
print()
print()
print()
print(func(data))


















































