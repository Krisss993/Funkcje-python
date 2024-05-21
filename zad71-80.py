# Napisz funkcję o nazwie concat(), która przyjmie dwie listy w formacie podanym jak poniżej:
l1 = [[1], [2],[5]]
l2 = [[3], [4],[6]]

# [[1, 3], [2, 4]]

def concat(l1, l2,):
    res = []
    for i,j in zip(l1,l2):
        res.append([i[0],j[0]])
    return res

print(concat(l1,l2))


# Napisz funkcję o nazwie identity(), która przyjmie za argument liczbę naturalną
# i zwróci macierz jednostkową reprezentowaną jako listę zagnieżdżoną.
def identity(n):
    res=[]
    one = 0
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(0)
        temp[one]=1
        one+=1
        res.append(temp)
    return res


print(identity(3))

def identity(n):
    res = [[0]* n for x in range(n)]
    for i in range(n):
        res[i][i]=1
    return res

print(identity(3))


# Napisz funkcję o nazwie fill_value(),
# która zwróci dwuwymiarową tablicę o rozmiarze height x width i wypełni ją stałą wartością value.

def fill_value(height=2, width=3, value=255):
    array = [[value]* width for _ in range(height)]
    return array

print(fill_value())


#Napisz funkcję o nazwie trace(), która zwróci ślad macierzy.
# Przekazana macierz musi być macierzą kwadratową.


def trace(array):
    res=0
    for y in range(len(array)):
        res += array[y][y]
    return res

print(trace([
    [1, 2],
    [4, 2]
]))

def trace(array):
    res=0
    for idx, item in enumerate(array):
        res+=item[idx]
    return res

print(trace([
    [1, 2],
    [4, 2]
]))

# Napisz funkcję o nazwie transpose(), która dokona transpozycji macierzy dwuwymiarowej (lista zagnieżdżona).


def transpose(array):
    width = len(array[0])
    res = []
    for i in range(width):
        pair = []
        for j in array:
            pair.append(j[i])
        res.append(pair)
    return res



print(transpose([
    [1, 2, 3],
    [4, 5, 6]
]))


# Zaimplementuj funkcję o nazwie max_prob(), która zwróci najwyższą wartość prawdopodobieństwa
# dla danego wiesza w macierzy dwuwymiarowej.
# Zakładamy, że użytkownik przekazuje macierz jako zagnieżdżoną listę o elementach nieujemnych
# oraz sumie w każdym wierszu równej 1.

def max_prob(array):
    res = []
    for i in array:
        res.append([max(i)])
    return res



print(max_prob([
    [0.3, 0.4, 0.3],
    [0.0, 0.1, 0.9]
]))

print()
print()
print()
# Wykorzystując poprzednie ćwiczenie zaimplementuj funkcję o nazwie detect_class(),
# która w miejscu najwyższej wartości prawdopodobieństwa w wierszu wstawi jedynkę oraz same zera poza
# (patrz poniżej).
# Zakładamy, że użytkownik przekazuje macierz jako zagnieżdżoną listę
# o elementach nieujemnych oraz sumie w każdym wierszu równej 1.







def detect_class(array):
    res = [[0]*len(array[0]) for x in array]
    pos = []
    for row in array:
        pos.append(row.index(max(row)))
    for i, y in zip(range(len(array)),pos):
            res[i][y]=1
    return res


print(detect_class([[0.3, 0.4, 0.2, 0.1], [0.0, 0.1, 0.7, 0.2], [0.0, 0.3, 0.3, 0.4]]) )




# Zaimplementuj funkcję o nazwie dot_product(),
# która przyjmie dwie listy tej samej długości (wektory) i policzy iloczyn skalarny.
# Zakładamy, że użytkownik przekazuje poprawnie zdefiniowany wektor.

def dot_product(l1,l2):
    res = []
    for x, y in zip(l1,l2):
        res.append(x*y)
    return sum(res)

print(dot_product([1, 2], [5, 2]))


# Napisz funkcję o nazwie count_none(), która policzy wszystkie brakujące wartości w liście.

def count_none(lst):
    res=0
    for x in lst:
        if x is None:
            res+=1
    return res


print(count_none([1, None, None, 5, None, 2]))

def count_none(lst):
    return lst.count(None)


print(count_none([1, None, None, 5, None, 2]))


# Napisz funkcję o nazwie top_n(), która z podanej listy wyciągnie top n największych wartości.

def top_n(lst,n):
    res = []
    for x in lst:
        if x not in res:
            res.append(x)
    return sorted(lst, reverse=True)[:3]



print(top_n([4, 5, 2, 9, 5, 2, 8, 2, 8, 10], 3))
