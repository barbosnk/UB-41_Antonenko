#задание 2
from random import *

arr = []
n = int(input('Введите размер матрицы: '))

for i in range(n):
    mat = [randint(1, 9) for i in range(n)]
    arr.append(mat)

for i in arr:
    print(*i)

print('-' * 10)

for i in arr:
    i[-1], i[0] = i[0], i[-1]
for i in arr:
    print(*i)
