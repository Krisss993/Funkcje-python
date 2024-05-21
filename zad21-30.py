# Zdefiniuj funkcję o nazwie calculate(),
# która przyjmie za argument listę i dokona następującego przekształcenia:
# wszystkie liczby nieparzyste mnoży przez 2
# W rozwiązaniu nie musisz uwzględniać walidacji danych wejściowych.

def calculate(lst):
    return [x*2 if x%2!=0 else x for x in lst]

#Zdefiniuj funkcję o nazwie sort_tuple(), która przyjmie za argument listę tupli o podanej strukturze:
list_of_tuples = [('mike', 34), ('bob', 41), ('john', 36), ('leo', 28)]
# I posortuje listę po drugim elemencie tupli. Oczekiwany wynik:

def sort_tuple(lst):
    return sorted(lst, key= lambda x:x[1])

print(sort_tuple(list_of_tuples))



# Zdefiniuj funkcję o nazwie replace_neg(),
# która przyjmie za argument listę liczb i każdą ujemną liczbę zastąpi 0.

def replace_neg(lst):
    return [x if x>0 else 0 for x in lst]

# Zdefiniuj funkcję o nazwie count(),
# która przyjmie za argument listę i zwróci liczbę liczb dodatnich oraz ujemnych
# (zero uznajemy za liczbę dodatnią) w podanej liście (patrz poniżej).

def count(lst):
    res1=0
    res2=0
    for x in lst:
        if x>=0:
            res1+=1
        else:
            res2+=1
    return (res1,res2)


# Zdefiniuj funkcję o nazwie preprocess(), która przyjmie za argument ciąg znaków poniższej postaci:

def preprocess(string):
    return int(i if i.isdigit() else '' for i in string)

def preprocess2(string):
    return string[2:].replace(',','')


# Zdefiniuj funkcję o nazwie make_hashtags(),
# która przyjmie za argument listę słów i zwróci ciąg hashtagów utworzonych z tych słów (patrz poniżej):

def make_hashtags(lst):
    return ' '.join('#'+word for word in lst)

print(make_hashtags(['gym', 'sport']))

# Zdefiniuj funkcję o nazwie convert(), która przyjmie za argument tekst w języku angielskim i
# zamieni wszystkie cyfry (nie liczby) w tekście na zapis słowny (patrz poniżej):


def convert(text):
    text = text.split(' ')

    dict={
        '1':'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
    }
    digits = dict.keys()

    for i, word in enumerate(text):
        if word in digits:
            text[i] = dict[word]
    return ' '.join(text)

print(convert('hello give me, 5 euros'))
print(convert('hello give me, 15 euros, 5'))


# Zdefiniuj funkcję o nazwie convert(), która będzie konwertować ciąg znaków zapisany jako
# snake_case na PascalCase (patrz poniżej):

#'some_important_function' -> 'SomeImportantFunction'
#'calculate_summary' -> 'CalculateSummary'

def convert(text):
    text = text.split('_')
    return ''.join(i.title() for i in text)


print(convert('hello_there'))


#Zdefiniuj funkcję o nazwie convert(), która będzie konwertować ciąg znaków zapisany jako snake_case na camelCase (patrz poniżej):

def convert(text):
    text = text.split('_')
    res=[text[0]]
    for i in range(1,len(text)):
        res.append(text[i].title())
    return ''.join(res)


print(convert('hello_there'))



# Zdefiniuj funkcję o nazwie preprocess(), która będzie przyjmować listę -
# strumień nazw plików i pozostawi tylko te nazwy plików, które kończą się na '.png' (patrz poniżej):

# ['img546.png', 'img243.png', 'img247.txt', 'img2456.pdf'] -> ['img546.png', 'img243.png']

def preprocess(lst):
    res=[]
    for word in lst:
        if word[-3:]=='png':
            res.append(word)
    return res

print(preprocess(['dsad.png','dass.dsa']))
