# Zdefiniuj funkcję is_palindrome(), która za argument przyjmie obiekt typu str
# i sprawdzi czy podany string jest palindromem
# (wyrażenie brzmiące tak samo czytane od lewej do prawej i od prawej do lewej).

def is_palindrome(text):
    if len(text)%2==0:
        first=text[:len(text)//2]
        second = text[len(text)//2:]
    else:
        first = text[:len(text) // 2+1]
        second = text[len(text) // 2:]
    return first==second[::-1]

print(is_palindrome('jaaj'))
print(is_palindrome('aja'))

def is_palindrome(text):
    return text==text[::-1]

print(is_palindrome('jaaj'))
print(is_palindrome('aja'))
print(is_palindrome('ajah'))

# Napisz funkcję sort_list(), która uporządkuje listę składającą się z dwuelementowych obiektów
# typu tuple według drugiego elementu tupli.

def sort_list(lst):
    return sorted(lst, key=lambda x:x[1])

print(sort_list([(1, 3), (4, 1), (4, 2), (0, 7)]))


# Rozważmy problem klasyfikacji binarnej uczenia maszynowego.
# Mamy daną listę y_true klas ze zbioru testowego oraz listę y_pred klas przewidzianych przez model:

y_true = [0, 0, 1, 1, 0, 1, 0]
y_pred = [0, 0, 1, 0, 0, 1, 0]

#Naszym zadaniem jest zbudowanie funkcji o nazwie accuracy(),
# która przyjmie dwa argumenty y_true oraz y_pred i policzy dokładność naszego modelu.
# Innymi słowy budujemy funkcję, która zwróci wskaźnik wartości prawidłowo przewidzianych przez model.
# Wynik zaokrąglij do 4 miejsca po przecinku.

def accuracy(y,y_pred):
    l = len(y)
    res=0
    for i, j in zip(y,y_pred):
        if i == j:
            res+=1/l
    return round(res,4)

print(accuracy(y_true,y_pred))


# MAE - Mean Absolute Error jest funkcją, która pozwala sprawdzić dokładność modelu uczenia maszynowego.
# MAE jest popularna w modelach regresyjnych.
# Dla dowolnych:
y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]
# [IN]: mae(y_true, y_pred)
# [OUT]: 0.325

def mae(y_true, y_pred):
    res=0
    for x,y in zip(y_true,y_pred):
        res+=abs(x-y)
    return round(res/len(y_true),4)

print(mae(y_true, y_pred))

# MSE - Mean Squared Error jest funkcją, która pozwala sprawdzić dokładność modelu uczenia maszynowego.
# MSE jest popularna w modelach regresyjnych.
y_true = [10, 10.5, 11.2, 10.4]
y_pred = [10.2, 10.4, 10.8, 11.0]
# [IN]: mse(y_true, y_pred)
# [OUT]: 0.142


def mse(y_true, y_pred):
    res=0
    for x,y in zip(y_true,y_pred):
        res+=abs(x-y)**2
    return round(res/len(y_true),3)

print(mse(y_true, y_pred))


# Zaimplementuj funkcję o nazwie relu(). ReLU - Rectified Linear Unit.
# Funkcja ta ma zastosowanie w sieciach neuronowych i dana jest wzorem:

def relu(x):
    if x<0:
        return 0
    else:
        return x

def relu(x):
    return max(0,x)

# Napisz funkcję o nazwie flatten(), która za argument przyjmie tak określoną listę i ją wypłaszczy,
# tzn. przedstawi w następującej postaci:
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

def flatten(data):
    res=[]
    for row in data:
        for nr in row:
            res.append(nr)
    return res

def flatten(data):
    res=[]
    for row in data:
        res.extend(row)
    return res


# Napisz funkcję o nazwie transfer_zeros(), która przyjmie za argument listę
# oraz zwróci tę listę zawierającą wszystkie zera na końcu.

def transfer_zeros(lst):
    zeroes = [x for x in lst if x==0]
    res=[x for x in lst if x!=0]
    res.extend(zeroes)
    return res


# odległość euklidesową definiujemy wzorem:

def euclidean_distance(p1,p2):
    diff = [(i-j)**2 for i,j in zip(p1,p2)]
    return sum(diff)**0.5

print(euclidean_distance([0, 3], [4, 0]))


# Zaimplementuj funkcję o nazwie arange(), która przyjmie trzy parametry:
# start, stop, step oraz wygeneruje listę składającą się z liczb całkowitych
# większych lub równych start oraz mniejszych niż stop.
# Parametr step domyślnie przyjmuje wartość 1 i oznacza rozmiar kroku.

def arange(start, stop, step=1):
    res=[]
    for i in range(start, stop, step):
        res.append(i)
    return res

