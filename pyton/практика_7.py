#вариант 3 №1
import math


def f(x, y):
    s = math.sqrt((x**2)+(y**2))
    return(s)


x = int(input())
y = int(input())
h1 = f(x, y)
x = int(input())
y = int(input())
h2 = f(x, y)
print (h1, h2)
if h1 == h2:
    print('Гипотенузы равны')
elif h1 < h2:
    print('Гипотенуза треугольника 1 меньше 2')
else:
    print('Гипотенуза треугольника 2 меньше 1')
#вариант 3 №2
def f(string):
    w = string.split() # Разделяем строку на отдельные слова
    so = [''.join(sorted(wo)) for wo in w]
    sorted_string = ' '.join(so) # Объединяем слова обратно в строку
    return sorted_string


s = input()
x = f(s)
print(x)
