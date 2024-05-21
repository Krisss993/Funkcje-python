# 11



l1= [[6, 2], [6, 3, 7], [3, 5]]
l2= [ [3],[4, 2], [0, 5, 1, 5]]


# def concat(l1,l2):
#     for i in range(len(l1)):
#         l1[i].extend(l2[i])
#     return l1
# print(concat(l1,l2))

# def concat2(l1,l2):
#     res=[]
#     for idx, item in enumerate(l1):
#         res.append(l1[idx])
#         res[idx].extend(l2[idx])
#     return res
#
# print(concat2(l1, l2))


# Zdefiniuj funkcję o nazwie concat(), która za dwa argumenty przyjmie dwie listy zagnieżdżone oraz
# zwróci nową listę, która połączy elementy list zagnieżdżonych na odpowiadających im pozycjach (patrz poniżej).
# Przed połączeniem list dokonaj pewnej walidacji wprowadzanych danych.
# Sprawdź, czy listy są tej samej długości.
# Jeśli nie, podnieś błąd ValueError z komunikatem 'The given lists are not of the same length.'

def concat(l1,l2):
    if len(l1) != len(l2):
        raise ValueError('The given lists are not of the same length.')
    else:
        res = []
        for idx, item in enumerate(l1):
            res.append(l1[idx])
            res[idx].extend(l2[idx])
        return res

print(concat(l1,l2))


# Zdefiniuj funkcję o nazwie sort_by_row(), która za argument przyjmie listę zagnieżdżoną (przykład poniżej):

data = [
    [4, 7, 2, 7, 9, 1],
    [6, 3, 2, 8, 8],
    [9, 7, 3, 2, 7]
]


def sort_by_row(lst):
    res = []
    for l in lst:
        res.append(sorted(x for x in l))
    return res

print(sort_by_row(data))



def sort_by_row2(lst):
    for row in lst:
        row.sort()
    return lst

print(sort_by_row(data))



# Zdefiniuj funkcję o nazwie top3(), która za argument przyjmie listę zagnieżdżoną (przykład poniżej):
# I zwróci trzy największe wartości z każdej wewnętrznej listy posortowane malejąco (patrz poniżej).
# Zakładamy, że każda wewnętrzna lista ma co najmniej trzy elementy.

data = [
    [4, 7, 2, 5, 9, 1, 3],
    [6, 3, 2, 8, 8, 7],
    [9, 7, 3, 2, 7, 2]
]

def top3(data):
    res = []
    for row in data:
        row = sorted(row, reverse=True)
        res.append(row[:3])
    return res

print(top3(data))


# Zdefiniuj funkcję o nazwie filter_users(), która za argument przyjmie listę zagnieżdżoną o podanej konstrukcji:
user_data = [
    {'user_id': '3546', 'level': 64, 'is_active': True},
    {'user_id': '3467', 'level': 34, 'is_active': False},
    {'user_id': '6673', 'is_active': True},
    {'user_id': '8454', 'level': 1, 'is_active': False},
    {'user_id': '3757', 'level': 63, 'is_active': True},
    {'user_id': '1668', 'is_active': False},
]

# I pozostawi tylko te słowniki, w których występuje klucz o nazwie 'level'.

def filter_users(data):
    return [dict for dict in data if 'level' in dict.keys()]

print(filter_users(user_data))



def filter_users2(data):
    return list(filter(lambda user:'level' in user.keys(), data))

print(filter_users2(user_data))




# Zdefiniuj funkcję o nazwie remove_repetitive(), która za argument przyjmie listę liczb
# i usunie liczby z powtarzającymi się cyframi (patrz poniżej).

def remove_repetitive(lst):
    res=[]
    for x in lst:
        if len(set(str(x))) == len(str(x)):
            res.append(x)
    return res

print(remove_repetitive([4543, 111, 357, 5675, 2567, 8632]))

def remove_repetitive2(lst):
    res=[]
    for x in lst:
        temp=''
        for i in str(x):
            temp += i
        if len(temp)==len(set(temp)):
            res.append(int(temp))
    return res


print(remove_repetitive2([4543, 111, 357, 5675, 2567, 8632]))

def remove_repetitive3(lst):
    return [x for x in lst if len(set(str(x))) == len(str(x))]

print(remove_repetitive3([4543, 111, 357, 5675, 2567, 8632]))



# Zdefiniuj funkcję o nazwie calculate(), która przyjmie dwa argumenty:
# listę składającą się z liczb
# liczbę naturalną k - domyślna wartość 5
# Funkcja ma zwracać wszystkie elementy listy, które są odległe od swoich sąsiadów (liczb sąsiednich)
# o wartość k lub większą.
# Elementy skrajne (pierwszy i ostatni element listy) należy pominąć w wyniku.
# W rozwiązaniu nie musisz uwzględniać walidacji danych wejściowych.

def calculate(lst, k=5):
    res=[]
    for i in range(1, len(lst)-1):
        if (abs(lst[i] - lst[i-1]) >= k) and (abs(lst[i] - lst[i+1]) >= k):
            res.append(lst[i])
    return res


print(calculate([2, 6, 2, 8, 1, 3, 10, 3]))
print(calculate([1, 6, 5, 2, 8, 11, 3, 10, 3],3))



from itertools import permutations

# Zdefiniuj funkcję o nazwie calculate(), która przyjmie za argument ciąg znaków - zdanie.
# Dla uproszczenia zakładamy, że tekst jest już oczyszczony ze znaków interpunkcyjnych i
# poszczególne słowa oddziela tylko znak spacji.
# Funkcja ma zwrócić listę wszystkich możliwych permutacji wyrazów przekazanego zdania (patrz poniżej).
def calculate2(text):
    all_permutations = permutations(text.split(' '))
    result_list = [' '.join(map(str, perm)) for perm in all_permutations]
    return result_list

print(calculate2('python is the'))

def calculate3(text):
    all_perm = permutations(text.split(' '))
    res = [' '.join(words) for words in all_perm]
    return res
print(calculate3('python is the'))

def calculate4(text):
    all_permutations = permutations(text.split(' '))
    result = [' '.join(map(str, perm)) for perm in all_permutations]
    return result

print(calculate4('python is the'))


# Zdefiniuj funkcję o nazwie create_mask(), która przyjmie dwie listy i zwróci listę będąca maskę logiczną
# - przyjmującą 1, gdy te listy mają tą samą wartość na odpowiadających pozycjach, przeciwnie 0.
# W rozwiązaniu nie musisz uwzględniać walidacji danych wejściowych.

def create_mask(l1, l2):
    res=[]
    for x, y in zip(l1,l2):
        if x == y:
            res.append(1)
        else:
            res.append(0)
    return res

def create_mask(l1, l2):
    return [1 if x==y else 0 for x,y in zip(l1,l2)]

# Zdefiniuj funkcję o nazwie distance(), która przyjmie dwie listy i zwróci
# odległość tych dwóch list mierzoną jako największą różnicę po odpowiadających elementach tych list.
# W rozwiązaniu nie musisz uwzględniać walidacji danych wejściowych.

def distance(l1,l2):
    return max([abs(i-j) for i,j in zip(l1,l2)])
