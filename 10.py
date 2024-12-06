n = 4
a = []
file = open('vvod.txt')
for i in file.readlines():
    n1 = int(i)
    a.append(n1)
a = [a]*n
for i in a:
    i[-1], i[0] = i[0], i[-1]
for i in a:
    print(*i)
print('-' * 10)

file_vivod = a
#print(file_vivod)
file_v = open('file_vivod.txt','w')
file_v.write(str(file_vivod))
file_v.close()
for i in a:
    print(*i)