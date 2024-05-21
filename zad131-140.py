# Rozważmy teraz operację XOR (alternatywa rozłączna - bitwise XOR) na liczbach binarnych.
# Operacja XOR (Exclusive OR) jest jedną z podstawowych operacji logicznych wykonywanych
# na dwóch wartościach binarnych. Działa ona na zasadzie porównywania bitów obu wartości i
# zwraca 1 (prawda) tylko wtedy, gdy jeden z bitów jest równy 1, a drugi bit jest równy 0.
# Jeśli oba bity są równe (zarówno 0, jak i 1), operacja XOR zwraca 0 (fałsz).


def decimal_to_binary(number):
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        result += str(number % 2)
        number = number // 2
    return result[::-1]

print(decimal_to_binary(110))

def bitwise_xor(n1,n2):
    if n1<0 or n2<0:
        raise ValueError('Both numbers must be positive.')
    else:
        str_n1=decimal_to_binary(n1)
        str_n2=decimal_to_binary(n2)
        max_len= max(len(str_n1), len(str_n2))
        equal_n1 = str_n1.zfill(max_len)
        equal_n2 = str_n2.zfill(max_len)
        res=''
        for i,j in zip(equal_n1,equal_n2):
            if (i == '0' and j == '1') or (i == '1' and j == '0'):
                res+='1'
            else:
                res+='0'
        return int(res,2)
print(bitwise_xor(10,140))


# Podsumowując, obiekt iterowalny redukujemy do pewnej wartości końcowej przy pomocy funkcji redukującej.
# W takim procesie występują trzy kroki:
# Wywołanie funkcji na pierwszych dwóch elementach obiektu iterowalnego i wygenerowanie częściowego wyniku
# Wywołanie funkcji na częściowym wyniku i kolejnym elemencie obiektu iterowalnego
# Powtarzanie procesu do momentu wyczerpania elementów w obiekcie iterowalnym i zwrócenie wyniku

def reduce(func, itr):
    if not itr:
        return None
    res = itr[0]
    for i in itr[1:]:
        res = func(res,i)
    return res


print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))




# Wczytaj plik cdr.csv. Możesz wykorzystać w tym celu moduł wbudowany csv.
# Wyodrębnij wszystkie ceny zamknięcia w postaci listy i przypisz do zmiennej closes:
# Chcemy wyznaczyć 3-dniową średnią kroczącą dla ceny close.
# Spróbuj zaimplementować w tym celu funkcję o nazwie moving_avg(),
# która za argument przyjmie listę cen zamknięcia i zwróci listę z wartościami dla 3-dniowej średniej kroczącej
# (poszczególne wartości średniej zaokrąglij do drugiego miejsca po przecinku).
# Zauważ, że liczba elementów listy z 3-dniową średnią kroczącą będzie krótsza od liczby
# z cenami zamknięcia o 2 elementy.
import pandas as pd
import numpy as np
def read_cdr():
    df = pd.read_csv('cdr.csv')
    res = df['Close'].values.tolist()
    return res



def moving_avg(lst):
    res = []
    for i in range(len(lst)-2):
        res.append( round(np.mean((lst[i:i+3])),2) )
    return res




print()
print()



import csv
def op():
    with open('cdr.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        columns = next(reader)
        rows = list(reader)
        closes = [row[4] for row in rows]
        return closes


print(op())
print('-------------------------')


def moving_mini(lst, n):
    res = []
    for i in range(len(lst)-(n-1)):
        res.append(min(lst[i:i+n]))
    return res

print(moving_mini(op(), 10))



# Chcemy wyznaczyć pewne poziomy wsparcia dla ceny. Na przykład 3-dniowe kroczące minimum
# dla ruchów na jedną sesję, 10-dniowe kroczące minimum dla ruchów krótkoterminowych, itd.
# Zaimplementowano w tym celu funkcję o nazwie moving_min(), która zwraca listę z wartościami
# dla minimum kroczącego o okresie window_size.
# Chcemy zachować jednak dodatkowy poziom bezpieczeństwa dla poziomów wsparcia
# i nieco odsunąć się od poziomów cenowych na których dochodziło do transakcji.
# Zaimplementuj funkcję o nazwie calculate_support(),
# która wyznaczy poziomy wsparcia dla ceny według opisanego poniżej wzoru:
# poziom wsparcia kroczącego = kroczące minimum n-okresowe - difference * ratio

print('-------------------------')
def difference():
    df = pd.read_csv('cdr.csv')
    res = (df['High']-df['Low']).values.round(2).tolist()
    return res

def low():
    with open('cdr.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        columns = next(reader)
        rows = list(reader)
        low = [row[2] for row in rows]
        return low

def high():
    with open('cdr.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        columns = next(reader)
        rows = next(reader)
        high = [row[3] for row in rows]
        return high




def calculate_support(lst, n, ratio=0.1):
    res= []
    mins = moving_mini(lst, n)
    for i, j in zip(mins, difference()):
        res.append(round(float(i) - (j*ratio),2))
    return res

print(calculate_support(op(),10))
print()
print()
print()

def calculate_support(prices, window_size, ratio=0.1):
    moving_mins = moving_mini(prices, window_size)
    diffs = difference()
    supports = [
        round(float(value) - (ratio * diff), 2)
        for value, diff in zip(moving_mins, diffs)
    ]
    return supports

print(calculate_support(op(),10))




with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    low = [row[2] for row in rows]
    high = [row[3] for row in rows]
    data = list(map(lambda row: (row[0], float(row[2]), float(row[3])), rows))


def max_min_diff(data):
    res = []
    for tuple in data:
        res.append(round(tuple[1]-tuple[2],2))
    return res

print(max_min_diff(data))


with open('cdr.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    columns = next(reader)
    rows = list(reader)
    data = list(map(lambda i: (i[0], float(i[1]), float(i[4])), rows))
    print(data)
def find_doji(data):
    swiece = []
    res = []
    for tuple in data:
        swiece.append(round(abs(tuple[1] - tuple[2]), 2))
    for date, swieca in zip(data, swiece):
        res.append(date[0])
    return res[swiece.index(min(swiece))]


print(find_doji(data))


class EmptyStackError(Exception):
    pass


class Stack:
    """The simplest stack."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError('The stack is empty.')
        return self._data.pop()

    def is_empty(self):
        return len(self._data) == 0


def is_palindrome(string):
    stack = Stack()
    is_palindrome_flag = True

    for char in string:
        stack.push(char)

    for char in string:
        if not char == stack.pop():
            is_palindrome_flag = False
    return is_palindrome_flag

print(is_palindrome('text'))
print(is_palindrome('textxet'))
