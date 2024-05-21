# Wykorzystując moduł wbudowany functools oraz klasę partial zbuduj z poniższej funkcji mul
# dwie funkcje o nazwach:
# double
# triple
# które odpowiednio będą podwajać i potrajać przekazaną wartość (będą przyjmować tylko jeden argument).
# Wystarczy tylko zaimplementować podane funkcje.
from functools import partial

def mul(x, y):
    return x * y

double = partial(mul, 2)
triple = partial(mul, 3)
mul(2,3)
print(double(5))


def div(x, y):
    return x/y

oneth = partial(div, 9)
print(oneth(3))


def power(x, y):
    return x ** y

square = partial(power, y=2)
cube = partial(power, y=3)
print(square(2))

# Rozważmy model kapitalizacji złożonej rocznej, gdzie:
# pv - oznacza wartość obecną kapitału
# r - oznacza stopę procentową (roczną)
# n - liczbę lat inwestycji
#
# Zaimplementuj funkcję o nazwie fv, która będzie wyznaczać wartość przyszłą kapitału zaokrągloną
# do drugiego miejsca po przecinku.

def fv(pv, i, n):
    return round(pv * (1 + i)**n,2)
print(fv(1000,0.03,5))


# Zaimplementuj funkcję o nazwie fv, która będzie wyznaczać wartość przyszłą kapitału
# w zależności od liczby okresów kapitalizacji w ciągu roku (argument m)
# zaokrągloną do drugiego miejsca po przecinku.

def fv(pv, i, n, m=1):
    return round(pv * (1 + i/m)**(n*m),2)


from functools import partial


def fv(rate, n, pv, m=1):
    return pv * (1 + (rate / m)) ** (n * m)


annual_acc_factor = partial(fv, pv=1, n=1)
print(annual_acc_factor(rate=0.04))


def stick(*args):
    res=[]
    for x in args:
        if type(x)==str:
            res.append(x)
    return '#'.join(res)


print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))


def stick(*args):
    return '#'.join([x for x in args if isinstance(x, str)])


print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))

def stick(*args):
    return '#'.join([x for x in args if type(x)==str])


print(stick('sport', 'summer'))
print(stick(3, 5, 7))
print(stick(False, 'time', True, 'workout', [], 'gym'))

# Zaimplementuj funkcję o nazwie display_info(), która wydrukuje nazwę firmy (tak jak poniżej)
# oraz w przypadku, gdy użytkownik przekaże także argument o nazwie price wydrukuje cenę
# (tak jak pokazano poniżej).

def display_info(company, **kwargs):
    print(f'Company name: {company}')
    if 'price' in kwargs:
        print(f'Price: ${kwargs['price']}')

display_info(company='CD Projekt', price=100)


# Znajdź sumę wszystkich liczb podzielnych przez 5 lub 7 mniejszych niż 100.
def calculate():
    nrs = range(0, 100, 1)
    res = []
    for x in nrs:
        if (x % 5 == 0 or x % 7 == 0):
            res.append(x)
    return sum(res)

print(calculate())


def calculate():
    return sum([x for x in range(100) if x % 5 == 0 or x % 7 == 0])

print(calculate())


def calculate():
    res = [0,1]
    a,b = 1,1
    n = 100
    for i in range(100):
        while b < 1000000:
            a,b = b, a+b
            if a%2==0:
                res.append(a)
    return res

print(calculate())


def calculate():
    res = 0
    a=0
    b=1
    while a < 1000000:
        if a % 2 == 0:
            res += a
        a, b = b, a + b
    return res

print(calculate())


def calculate():
    res = 0
    a = 0
    b = 1
    while a < 1000000:
        if a % 2 == 0:
            res += a
        a, b = b, a + b
    return res


print(calculate())
