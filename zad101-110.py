

def compress(n):
    number_str=str(n)
    counter = 1
    res=[]
    curr_value=number_str[0]
    for i in range(1,len(number_str)):
        if curr_value==number_str[i]:
            counter+=1
        else:
            res.append(curr_value)
            res.append(counter)
            counter=1
            curr_value=number_str[i]
    res.append(curr_value)
    res.append(counter)
    return res


print(compress(6665551111))


# Algorytm przechodzi od lewej do prawej przez poszczególne cyfry i zwraca obiekt typu str.
# Każda napotkana cyfra jest zapisywana wraz z liczbą powtórzeń danej cyfry za pomocą kropek
# do momentu napotkania kolejnej, innej cyfry w liczbie.

from itertools import groupby
def compress(n):
    number_str = str(n)
    res=''
    for nr, group in groupby(number_str):
        dots = len(list(group))
        res+=nr+int(dots)*'.'
    return res


print(compress(11114444488))
print(compress(11))
print(compress(111))
print(compress(1))



# Zaimplementuj funkcję o nazwie decompress(), która pozwoli otrzymany wynik kompresji przekształcić z
# powrotem do liczby.

from itertools import groupby


def compress(number):
    result = []
    for key, group in groupby(str(number)):
        result.append((key, str(len(list(group)))))
    result = [''.join(item) for item in result]
    return '_'.join(result)


def decompress(number_str):
    lst = number_str.split('_')
    res=''
    for i in lst:
        res+=i[0]*int(i[1])
    return int(res)
print(decompress('14_53_22_51_02'))

# Dla wektorów tak zdefiniowanych możemy określić odległość Hamminga.
# Odległość Hamminga wektorów u i v to liczba elementów, gdzie wektory u i v są różne.

def hamming_distance(u, v):
    res=0
    if len(u) != len(v):
        raise ValueError('Both vectors must be the same length.')
    for i, j in zip(u,v):
        if i!=j:
            res+=1
    return res


print(hamming_distance('1010101','1110110'))


def hamming_weight(u):
    return str(u.count('1'))

print(hamming_weight('123123'))

print()
print()

# Poniżej zestaw punktowy dla wersji w języku angielskim:
# pusta płytka - 0 pkt (najczęściej dwie w zestawie)
# EAIONRTLSU - 1 pkt
# DG - 2 pkt
# BCMP - 3 pkt
# FHVWY - 4 pkt
# K - 5 pkt
# JX - 8 pkt
# QZ - 10 pkt
# Zaimplementuj funkcję o nazwie score(), która będzie zwracać wynik dla ułożonego słowa.
# Zakładamy, że przekazane słowo jest poprawne w sensie gramatycznym.
# Pustą płytkę dla prostoty możemy przedstawić jako znak spacji ' '.

def score(word):
    dict = {
        'EAIONRTLSU': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10,
        ' ':0
    }

    res=0
    for i in word.upper():
        for k, v in dict.items():
            for j in k:
                if i==j:
                    res+=v
    return res

print(score('hello'))
print(score('hello there'))


from collections import ChainMap


def score(word):
    dict = {
        'EAIONRTLSU': 1,
        'DG': 2,
        'BCMP': 3,
        'FHVWY': 4,
        'K': 5,
        'JX': 8,
        'QZ': 10,
        ' ':0
    }


    scores = ChainMap(*[dict.fromkeys(l, score) for l, score in dict.items()])
    return sum(scores[l.upper()] for l in word)

print(score('hello'))
print(score('hello there'))


# Rozważmy poniższy problem. Mamy podaną sekwencję znaków i chcemy z niej wydobyć wszystkie podciągi o długości n w kolejności,
# w jakiej się pojawiają w sekwencji.
# Na przykład z sekwencji znaków 'python' możemy wydobyć 3-cyfrowe serie:

def get_slices(text, n):
    if n < 1:
        raise ValueError ('The length cannot be less than 1.')
    elif len(text) < n:
        raise ValueError ('The length cannot be greater than sequence.')
    else:
        res = []
        for i in range(len(text)+1-n):
            res.append(text[i:n+i])
        return res


print(get_slices('esmartdata', 5))
print(get_slices('654646849173', 6))

def get_slices(text, n):
    if n < 1:
        raise ValueError ('The length cannot be less than 1.')
    elif len(text) < n:
        raise ValueError ('The length cannot be greater than sequence.')
    else:
        return [text[i:n+i] for i in range(len(text)+1-n)]


print(get_slices('esmartdata', 5))
print(get_slices('654646849173', 6))


# Zaimplementuj funkcję o nazwie spiral_matrix(), która za argument przyjmie stopień macierzy i wygeneruje macierz
# w porządku spiralnym o podanym stopniu. Rozwiązanie przedstaw w postaci list zagnieżdżonych.

def spiral_matrix(n):
    matrix = [[0] * n for _ in range(n)]  # Inicjalizacja macierzy zerami
    num = 1  # Początkowa wartość
    start_row, end_row, start_col, end_col = 0, n-1, 0, n-1

    while start_row <= end_row and start_col <= end_col:
        # Wypełnij górny wiersz
        for i in range(start_col, end_col + 1):
            matrix[start_row][i] = num
            num += 1
        start_row += 1

        # Wypełnij prawą kolumnę
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = num
            num += 1
        end_col -= 1

        # Wypełnij dolny wiersz
        if start_row <= end_row:
            for i in range(end_col, start_col - 1, -1):
                matrix[end_row][i] = num
                num += 1
            end_row -= 1

        # Wypełnij lewą kolumnę
        if start_col <= end_col:
            for i in range(end_row, start_row - 1, -1):
                matrix[i][start_col] = num
                num += 1
            start_col += 1

    return matrix

# Przykład użycia
degree = 7
result_matrix = spiral_matrix(degree)

# Wydrukuj wynik
for row in result_matrix:
    print(row)

# Zaimplementuj funkcję o nazwie clean_hashtags(), która wczyta dołączony plik hashtags.txt
# oraz dokona pewnego czyszczenia hashtagów. Czyszczenie polega na pozostawieniu hashtagów o maksymalnej długości 4 znaków.
# Znak '#' nie jest wliczany do długości hashtagu. Przykładowo hashtag '#gym' ma długość 3.

# Zadbaj także o usunięcie duplikatów jeśli takie występują.
# Następnie oczyszczone i posortowane alfabetycznie hashtagi zwróć w postaci listy.

def clean_hashtags():
    with open('hashtags.txt','r') as file:
        text = file.read()
        res = [x for x in text.split() if len(x)<=5]
    return sorted(list(set(res)))

print(clean_hashtags())


def clean_hashtags(input, output, max_l):
    with open (input, 'r') as input_file:
        text = input_file.read()
        res = sorted(set([x for x in text.split() if len(x) <= max_l+1]))
    with open(output, 'w') as output_file:
        for x in res:
            output_file.write(x+'\n')



clean_hashtags('hashtags.txt', 'output.txt', 5)

def clean_hashtags(input_file, output_file, length):
    with open(input_file, 'r') as file:
        content = file.read()
    hashtags = content.split()
    short = [htag for htag in hashtags if len(htag) <= length + 1]
    unique_short = sorted(set(short))
    with open(output_file, 'w') as file:
        for hashtag in unique_short:
            file.write(hashtag + '\n')


clean_hashtags('hashtags.txt', 'output2.txt', 5)
