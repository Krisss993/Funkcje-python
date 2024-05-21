# Zdefiniuj funkcję o nazwie preprocess(), która za argument będzie przyjmować listę krotek (tupli)
# i usunie z tej listy wszystkie jednoelementowe krotki (tuple)

def preprocess(lst):
    res = []
    for x in lst:
        if len(x)>1:
            res.append(x)
    return res
print(preprocess([(4, 5), (4, ), (5, 2), (5, 3, 2), (5, )]))


# Zdefiniuj funkcję o nazwie preprocess(), która za argument będzie przyjmować listę krotek (tupli)
# i usunie z tej listy wszystkie krotki zawierające tylko wartości None (patrz poniżej):

def preprocess(lst):
    res = []
    for x in lst:
        if not x.count(None) == len(x):
            res.append(x)
    return res

print(preprocess([(5, None), (None,), (3, None, None), (None, None)]))


def preprocess(lst):
    res = []
    for x in lst:
        if not all(i==None for i in x):
            res.append(x)
    return res

print(preprocess([(5, None), (None,), (3, None, None), (None, None)]))


# Zdefiniuj funkcję o nazwie flatten(), która za argument będzie przyjmować zagnieżdżoną
# listę lub krotkę i zwracać jej wypłaszczoną formę (patrz poniżej):

def flatten(data):
    res=[]
    for lst in data:
        for item in lst:
            res.append(item)
    return res

print(flatten(([5], [6], [2, 4, 2], [3, 4])))


def flatten(data):
    return [item for lst in data for item in lst]

print(flatten(([5], [6], [2, 4, 2], [3, 4])))

# Zdefiniuj funkcję o nazwie flatten(), która za argument będzie przyjmować zagnieżdżoną krotkę list,
# które to będą składać się z wyrazów (patrz poniżej):

# (['apple'], ['gym', 'fit'], ['movie', 'netflix'])

# Funkcja ma przetworzyć podaną krotkę i zwrócić jeden ciąg będący ciągiem hashtagów utworzonych
# z podanych słów:

def flatten(data):
    res=[]
    for lst in data:
        for item in lst:
            res.append('#'+item)
    return ' '.join(res)


print(flatten((['apple'], ['gym', 'fit'], ['movie', 'netflix'])))

def flatten(data):
    return ' '.join(['#'+item for lst in data for item in lst])

print(flatten((['apple'], ['gym', 'fit'], ['movie', 'netflix'])))


# Załóżmy, że pozyskujesz strumień danych postaci data:
# Zdefiniuj funkcję o nazwie calculate(), która za argument będzie przyjmować słowniki powyższej postaci
# i zwracać poniższe statystki:
# temperaturę minimalną
# temperaturę maksymalną
# temperaturę średnią - wynik zaokrąglij do dwóch miejsc po przecinku
data = {
    'device_id': '3057304985',
    'temp': [23.5, 22.0, 23.1, 25.5, 24.1],
    'city': 'Warsaw',
    'country': 'Poland'
}



def calculate(data):
    avg1 = round(sum(data['temp'])/len(data['temp']),2)
    max1=max(data['temp'])
    min1=min(data['temp'])
    return (min1,max1,avg1)

print(calculate(data))


# Załóżmy, że pozyskujesz strumień danych postaci data:
# Zdefiniuj funkcję o nazwie convert(), która za argument będzie przyjmować słowniki powyższej postaci
# i konwertować je na listy zagnieżdżone o poniższej postaci:
data = {
    'device_id': '3057304985',
    'temp': [23.5, 22.0, 23.1, 25.5, 24.1],
    'city': 'Warsaw',
    'country': 'Poland'
}

def convert(data):
    res = []
    for k,v in data.items():
        res.append([k,v])
    return res

print(convert(data))


# Załóżmy, że pozyskujesz strumień danych postaci data:
# Zdefiniuj funkcję o nazwie to_csv(), która za argument będzie przyjmować słowniki powyższej postaci
# i zwracać dane dotyczące temperatury w formacie CSV:
data = {
    'device_id': '3057304985',
    'temp': [23.5, 22.0, 23.1, 25.5, 24.1],
    'city': 'Warsaw',
    'country': 'Poland'
}

def to_csv(data):
    res=[]
    for v in data['temp']:
        res.append(str(v))
    return 'temp,'+','.join(res)

print(to_csv(data))


def to_csv(data):
    return 'temp,'+ ','.join(str(x) for x in data['temp'])

print(to_csv(data))


# Zdefiniuj funkcję o nazwie acronym(), która za argument będzie przyjmować ciąg znaków
# - wyrazów i zwracać akronim podanego ciągu wyrazów (patrz poniżej):

def acronym(text):
    return ''.join([i[0].upper() for i in text.split(' ')])

print(acronym('hello there'))


# Zdefiniuj funkcję o nazwie collatz(), która będzie przedstawiać problem Collatza.
# Problem można podsumować w następujący sposób:

# Weź dowolną dodatnią liczbę całkowitą n.
# Jeśli n jest parzyste, podziel n przez 2, aby uzyskać n/2.
# Jeśli n jest nieparzyste, pomnóż n przez 3 i dodaj 1, aby uzyskać 3n + 1.
# Powtarzaj proces w nieskończoność.
# Hipoteza mówi, że bez względu na to, od jakiej liczby zaczniesz, w końcu zawsze osiągniesz 1.

def collatz(n):
    count=0
    while n!=1:
        count+=1
        if n%2==0:
            n=n/2
        else:
            n=n*3+1
    return n, count

print(collatz(8))


# Zdefiniuj funkcję o nazwie get_chunks(), która będzie przyjmować dwa argumenty:
# text - ciąg znaków
# num - liczbę znaków w jednym kawałku po podziale
# I podzieli podany ciąg znaków na mniejsze kawałki o długości num.

from math import ceil
def get_chunks(text,n):
    res=[]
    for i in range(0,len(text),n):
        res.append(text[i:i+n])
    return res

print(get_chunks('hello there',3))

def get_chunks(text,n):
    if len(text)<n:
        return [text]
    print([text[:n]])
    print(get_chunks(text[n:],n))
    return [text[:n]] + get_chunks(text[n:],n)

print(get_chunks('hello there',3))

