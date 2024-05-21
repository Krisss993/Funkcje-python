# Zdefiniuj funkcję o nazwie maximum(), która zwróci maksimum z dwóch liczb.
# Użyj instrukcji warunkowej.

def maximum(x1,x2):
    if x1>x2:
        return x1
    return x2


# Zdefiniuj funkcję o nazwie maximum(), która zwróci maksimum z trzech liczb. Użyj instrukcji warunkowej.

def maximum(x1,x2,x3):
    if x1>x2 and x1>x3:
        return x1
    elif x2>x3:
        return x2
    return x3

# Zdefiniuj funkcję o nazwie multi(), która jako parametr przyjmie obiekt iterowalny (lista, tupla)
# oraz zwróci iloczyn wszystkich elementów listy.

def multi(lst):
    res=1
    for i in lst:
        res*=i
    return res

# Napisz funkcję o nazwie map_longest(), która przyjmie listę słów i zwróci długość najdłuższego słowa.

def map_longest(lst):
    return max(len(x) for x in lst)

# Napisz funkcję o nazwie filter_ge_6(),
# która przyjmie listę słów i zwróci słowa o długości większej lub równej 6 znaków.

def filter_ge_6(lst):
    res=[]
    for word in lst:
        if len(word)>=6:
            res.append(word)
    return res


# Napisz funkcję o nazwie factorial(), która obliczy wartość silni z danej liczby.

def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

print(factorial(2))
print(factorial(4))
print(factorial(6))

def factorial(n):
    if n==0:
        return 1
    print(n*factorial(n-1))
    return n*factorial(n-1)

print(factorial(2))
print(factorial(4))
print(factorial(6))


# Napisz funkcję count_str(), która zwróci liczbę obiektów typu str w obiekcie iterowalnym (list, tuple, set).

def count_str(lst):
    res=0
    for i in lst:
        if type(i)==str:
            res+=1
    return res

# Napisz funkcję count_str(),
# która zwróci liczbę obiektów typu str o długości powyżej 2 znaków w obiekcie iterowalnym (lista, tuple, set).

def count_str(lst):
    res=0
    for i in lst:
        if type(i)==str:
            if len(i)>2:
                res+=1
    return res

# Napisz funkcję remove_duplicates(), która usunie duplikaty z listy (kolejność elementów nie musi być zachowana).

def remove_duplicates(lst):
    return set(lst)

# Napisz funkcję is_distinct(), która sprawdzi, czy lista zawiera unikalne wartości.

def is_distinct(lst):
    return len(lst)==len(set(lst))

