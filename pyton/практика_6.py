#вариант 3 №1
n = int(input())
d = [i for i in range(n+1)]
y =d[1::2]
y1 = sum(y)
print(d)
print(y1)
#вариант 3 №2
d = [int(input())for i in range(8)]
for i in range(len(d)):
    if d[i]<15:
        d[i] *=2
print(d)