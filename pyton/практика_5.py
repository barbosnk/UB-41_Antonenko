#вариант №3
s = str(input())
x = len(s) - len(s.replace(".", ""))
print(s.replace(".",""))
print(str(x))
#вариант №4
s = str(input())
y = s.replace("o","t")
x = y.replace("a","o")
s1 = "o"
print('x.count = ',x.count(s1))
print(len(x))