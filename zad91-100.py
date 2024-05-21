# Rozkład liczby na czynniki pierwsze polega na zapisaniu dowolnej liczby naturalnej
# za pomocą iloczynu liczb pierwszych. Żeby rozłożyć liczbę na czynniki pierwsze należy
# daną liczbę dzielić (bez reszty) przez liczby pierwsze do momentu, aż zostanie tylko liczba 1.

def calculate(n):
    i=2
    res = []
    while i*i <= n:
        if not n % i == 0:
            i+=1
        else:
            n = n//i
            res.append(i)
    if n > 1:
        res.append(n)
    return res




print(calculate(88))



def calculate(n):
    i=2
    res = []
    while i*i<=n:
        if n%i==0:
            n=n//i
            res.append(i)
        else:
            i+=1
    if n>1:
        res.append(n)
    return res



print(calculate(88))





























# Rozkład liczby na czynniki pierwsze polega na zapisaniu dowolnej liczby naturalnej za pomocą iloczynu
# liczb pierwszych. Żeby rozłożyć liczbę na czynniki pierwsze, należy daną liczbę dzielić (bez reszty)
# przez liczby pierwsze do momentu, aż zostanie tylko liczba 1.



def calculate(n):
    i=2
    res = []
    while i*i<n:
        print('i: ',i, '  n: ',n)
        if n%i==0:
            n=n//i
            res.append(i)
        else:
            i+=1
    if n>1:
        res.append(n)
    print(res)
    return max(res)

print(calculate(88))

# Rozważmy liczby palindromiczne. Liczba palindromiczna lub inaczej symetryczna to liczba,
# która nie zmienia się po zapisaniu jej cyfr w odwrotnej kolejności.

def calculate():
    onethree=range(1,10)
    middle=range(0,10)
    return len(onethree)*len(middle)

print(calculate())

def calculate():
    res=[]
    for i in range(100,1000):
        if str(i)==str(i)[::-1]:
            res.append(i)
    return len(res)

print(calculate())


# Zaimplementuj funkcję, która zwróci największą liczbę palindromiczną powstałą z iloczynu liczb dwucyfrowych

def calculate():
    res = []
    for i in range(10,100):
        for j in range(10,100):
            if str(i*j)==str(i*j)[::-1]:
                res.append(i*j)
    return res

print(calculate())

# Największy wspólny dzielnik (Greatest Common Divisor - GCD)

def greatest_common_divisor(n1,n2):
    d1= []
    d2 = []
    for i in range(1,n1+1):
        if n1%i==0:
            d1.append(i)
    for j in range(1,n2+1):
        if n2%j==0:
            d2.append(j)
    return max(set(d1)&set(d2))

print(greatest_common_divisor(100,200))

def is_prime(n):
    res=[]
    if n>1:
        for i in range(2,n+1):
            if n%i==0:
                res.append(i)
    print(res)
    return len(res)==1

print(is_prime(11))
print(is_prime(2))
print(is_prime(5))
print(is_prime(123))


def calculate():
    res=[]
    for i in range(1,1000):
        if is_prime(i):
            res.append(i)
    print(res)
    return res[99]

print(calculate())

def calculate():
    counter = 0
    n = 2
    while True:
        if is_prime(n):
            counter+=1
            if counter==100:
                return n
        n+=1
print(calculate())


# Zaimplementuj funkcję o nazwie is_palindrome(), która sprawdzi, czy przekazana liczba jest palindromiczna
# w zapisie dziesiętnym oraz w zapisie binarnym.

def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]

print(is_palindrome(29492))
print(is_palindrome(363))

# Zaimplementuj funkcję o nazwie calculate(), która zwróci wszystkie trzycyfrowe liczby palindromiczne
# zarówno pod względem zapisu dziesiętnego jak i binarnego. W odpowiedzi wywołaj funkcję calculate()
# i wydrukuj wynik do konsoli.
def is_palindrome(number):
    if str(number) != str(number)[::-1]:
        return False
    bin_number = bin(number)[2:]
    return bin_number == bin_number[::-1]


def calculate():
    res = []
    for i in range(100, 1000):
        if is_palindrome(i):
            res.append(i)
    return res

print(calculate())


from itertools import groupby
def compress(n):

    res = []
    for key, group in groupby(str(n)):
        print(list(group))
        res.append((key, len(list(group))))
    return res


print(compress(1002222200))


def compress(n):
    number=str(n)
    res = []
    count=1
    current = number[0]
    for i in range(1,len(number)):
        if current==number[i]:
            count+=1
        else:
            res.append((current,count))
            current = number[i]
            count=1
    res.append((current, count))
    return res


print(compress(1002222200))












from itertools import groupby

def compress(n):
    number=str(n)
    counter=[]
    nrs=[]
    res=''
    for values, lst in groupby(number):
        counter.append(len(list(lst)))
        nrs.append(values)
    print(counter)
    print(nrs)
    for i, j in zip(counter, nrs):
        res+=j+str(i)+'_'
    return res.strip('_')

print(compress(11212123))
print(compress(100000))




