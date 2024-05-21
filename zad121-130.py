# Zaimplementuj funkcję o nazwie encrypt(), która przyjmie trzy argumenty:
# alphabet - alfabet, który chcemy zaszyfrować
# message - wiadomość, którą chcemy zaszyfrować
# key - klucz, przesunięcie


def generate_cipher(alpha, key=2):
    res = ''
    for i in range(len(alpha)):
        res+=alpha[(i+key)%len(alpha)]
    return res


alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(generate_cipher(alpha, 2))

# # # @@  @@ @  @2 @ @ 2 2 2 2 @ @ @ @
def encrypt(alphabet, word, key=2):
    res = ''
    word=word.upper()
    cipher = generate_cipher(alphabet, key)
    for letter in word:
        if letter in alphabet:
            res += cipher[alphabet.index(letter)]
        else:
            res+=letter
    return res


alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print(encrypt(alpha, 'hello',2))


def decrypt(alphabet, word, key=2):
    word=word.upper()
    crypted = encrypt(alphabet, word, key*(-1))
    return crypted


print(decrypt(alpha, 'fcjjm'))
print(decrypt(alpha, 'RAVJQP'))


#
MORSE_CODE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '&': '.-...',
    '@': '.--.-.',
    ':': '---...',
    ',': '--..--',
    '.': '.-.-.-',
    ''': '.----.',
    ''': '.-..-.',
    '?': '..--..',
    '/': '-..-.',
    '=': '-...-',
    '+': '.-.-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-',
    '!': '-.-.--',
}

def encrypt(message):
    res = ''
    for letter in message.upper():
        if letter in MORSE_CODE.keys():
            res+=MORSE_CODE[letter]+' '
        else:
            res+='/ '
    return res[:-1]

print(encrypt('hello there'))
print(encrypt('ROGER THAT'))


# ## 3 3 3 3 3## ### # # 3 ## #  ## 3 # # 333




MORSE_CODE_REVERSED = {val: key for key, val in MORSE_CODE.items()}


def encrypt(message):
    return ' '.join([
        MORSE_CODE[char.upper()] if char != ' ' else '/'
        for char in message
    ])


def decrypt(message):
    decipher = ''
    for char in message.split():
        if char != '/':
            decipher += MORSE_CODE_REVERSED[char]
        else:
            decipher += ' '
    return decipher

# $$  $4 4 4 4  $$44 4 $ 44 4 4 4 4 4 4 4 4 $

# pole_kola = pole_kwadratu * (liczba_wylosowanych_punktów_wewnątrz_koła / liczba_wszystkich_wylosowanych_punktów)
import random



def generate_random_point():
    return random.uniform(-1, 1), random.uniform(-1, 1)


def is_in_unit_circle(point):
    return point[0] ** 2 + point[1] ** 2 <= 1


points = [generate_random_point() for _ in range(15)]
flags = [is_in_unit_circle(point) for point in points]
print(flags)

def estimate():
    return sum(flags)/len(flags)*4

print(estimate())

print()
print()
print()
print()


# Ćwiczenie 127
# Rozważmy metodę Monte Carlo. Jest to metoda stosowana do modelowania matematycznego procesów dość złożonych,
# w celu wyznaczenia przybliżonego wyniku za pomocą podejścia analitycznego.
# Ważną rolę w tej metodzie odgrywa losowanie wielkości charakteryzujących proces.
# Wykorzystamy metodę Monte Carlo do wyznaczenia przybliżenia liczby Pi.
# Rozważmy okrąg o promieniu 1 i środku w początku układu współrzędnych (przestrzeń R^2).
# Pole koła o tak zdefiniowanym okręgu jest równe dokładnie Pi.
# Dodajmy do tego kwadrat opisany na tym okręgu o wierzchołkach w punktach (1, 1), (1,-1), (-1, -1), (-1, 1).
# Bok tego kwadratu ma długość 2 a jego pole wynosi 4.
# Naszym zadaniem jest losowanie punktów z podanego kwadratu zgodnie z rozkładem jednostajnym i sprawdzanie,
# czy wylosowany punkt wpada nam do okręgu. Prawdopodobieństwo takiego zdarzenia jest równe
# polu koła o promieniu 1, czyli dokładnie Pi.
# Liczbę symulacji dobieramy dowolnie, natomiast zasadniczo im więcej symulacji przeprowadzimy
# tym lepsze uzyskamy przybliżenie liczby Pi.
# Pojedyncza symulacja: Losujemy punkt z kwadratu zgodnie z rozkładem jednostajnym i sprawdzamy,
# czy leży wewnątrz podanego okręgu.

import random
import numpy as np


def generate_random_point():
    return (random.uniform(-1, 1), random.uniform(-1, 1))


print(generate_random_point())

def is_in_unit_circle_point(point):
    return point[0]**2+point[1]**2<=1


def is_in_unit_circle(n):
    points = [generate_random_point() for _ in range(n)]

    return [is_in_unit_circle_point(point) for point in points]

print(is_in_unit_circle(15))


def estimate(n):
    return (4*sum(is_in_unit_circle(n)))/n

print(estimate(10000))


# System binarny lub inaczej dwójkowy system liczbowy to pozycyjny system liczbowy,
# w którym podstawą jest liczba 2, a do zapisu liczb wykorzystywane są tylko dwie cyfry 0 i 1.
# Liczby zapisuje się jako ciągi cyfr, z których każda jest mnożoną kolejnej potęgi liczby 2.
# Na przykład liczbę 10 zapisaną w systemie dwójkowym możemy przedstawić jako 1010, ponieważ:
# 1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0 = 8 + 0 + 2 + 0 = 10

def decimal_to_binary(n):
    res=''
    if n == 0:
        return '0'
    while n > 0:
        res += str(n%2)
        n=n//2
    return res[::-1]

print(decimal_to_binary(17))

print()
print()

def bitwise_and(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError('Both numbers must be positive.')
    else:
        n1 = decimal_to_binary(n1)
        n2 = decimal_to_binary(n2)
        max_l = max(len(n1), len(n2))
        n1 = n1.zfill(max_l)
        n2 = n2.zfill(max_l)
        res=''
        for i,j in zip(n1,n2):
            if i=='1' and j=='1':
                res+='1'
            else:
                res+='0'
        return int(res, 2)

print(bitwise_and(10,140))

# Zaimplementuj funkcję o nazwie bitwise_or(), która za argumenty przyjmie dwie liczby naturalne
# (w zapisie dziesiętnym) i zwróci wynik operacji alternatywy bitowej w zapisie dziesiętnym.
# Do przekształcenia liczby z zapisu binarnego na dziesiętny można wykorzystać int().
# W przypadku, gdy którykolwiek przekazany argument jest mniejszy od zera podnieś błąd ValueError z komunikatem:
# Rozważmy teraz operację OR (alternatywa bitowa - bitwise OR) na liczbach binarnych.
# Operację stosuje się do par liczb naturalnych wykonując operacje na cyfrach zapisów binarnych tych liczb.
# Wynik zawiera zera na pozycjach, na których w obydwu ciągach występowały zera, przeciwnie jedynki


def bitwise_or(n1, n2):
    if n1 < 0 or n2 < 0:
        raise ValueError('Both numbers must be positive.')
    else:
        n1 = decimal_to_binary(n1)
        n2 = decimal_to_binary(n2)
        max_l = max(len(n1), len(n2))
        n1 = n1.zfill(max_l)
        n2 = n2.zfill(max_l)
        res=''
        for i,j in zip(n1,n2):
            if i=='0' and j=='0':
                res+='0'
            else:
                res+='1'
        return int(res, 2)

print(bitwise_or(10,140))


