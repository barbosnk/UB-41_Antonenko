#задание №3
a = int(input('a = '))
b = int(input('b = '))
x = []
if a<b:
    print('a должно быть больше b')
for i in range(b+1,a):
    if i%2!=0:
        x.append(i)
print(x[::-1])
#задание №4
n = int(input('n = '))
total = sum(range(n+1))
print(total)