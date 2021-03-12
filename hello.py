# -*- coding: utf-8 -*-
print("Olá Mundo!")

print(2 ** 3) #exponenciação

print(10 / 3)

x = False
y = True

print(not y)
print(x or y)
print(x and y)
print(not(x and y))

if x and y :
    print('qualquer coisa')
elif not x:
    print("coisa e tal")
else:
    print("outra coisa")

z = 1
while z < 10:
    print(z)
    z += 1

xx = {"teste": False}
lista = ['Teste', xx, True, False, [1,2,3], 3,5, 34.5]
print(xx["teste"])
for item in lista:
    print(item)


for i in range(0, 110, 10):
    print(i)


