import math
#первое задание
x=0.4*(10**4)
y=(-0.875)
z=(-0.475*(10**(-3)))
s = abs(math.cos(x) - math.cos(y)) ** ((1 + 2 * math.sin(y)**2)) * (1 + z + (z * z) / 2 + (z * z * z) / 3 + (z * z * z * z) / 4)
print("s = {0:.5f}".format(s))
#второе задание
x = (-15.246)
y = (4.642*(10**(-2)))
z = 21
s = math.log(y**(-math.sqrt(abs(x)))) * (x-y/2)
print("s = {0:.3f}".format(s))


