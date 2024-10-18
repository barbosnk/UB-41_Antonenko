#задание №1
a = int(input())
b = int(input())
c = int(input())
if a <= 3 and a >= 1:
    print(a, 'входит')
if b <= 3 and b >= 1:
    print(b, 'входит')
if c <= 3 and c >= 1:
    print(c, 'входит')
#задание №1.2
a = int(input())
if a%11 == 0 and a < 100:
    print('да')
else:
    print('нет')
#задание №2.3
a = int(input('a'))
b = int(input('b'))
c = 0
if a<b:
    c = a + b
elif a>b and a>3:
    c =b**2 - b
else:
    c = b**2 - 1
print('c =',c)
#задание №2.4
v = int(input('v ='))
k = int(input('k ='))
z = 0
if v<k:
    z = v-k+1
elif k>v:
    z = k**2 - v**2
else:
    z = k**2 - k
print('z =',z)
#задание №3.3
x=[]
y=[]
v = input('v = ')
for i in v:
    if int(i) % 2==0:
        x.append(i)
    else:
        y.append(i)
print(x)
print(y)
#задание №3.4
v = int(input())
k = 0
for i in range (2,v-1):
    if v%i == 0:
        k+=1
if k<=0:
    print('Число простое')
else:
    print('Число не простое')
    