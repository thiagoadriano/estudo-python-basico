lista = ["qualquer", "coisa", 3, True, 4.9]

lista.append("outro")
print(lista)

lista2 = lista.copy()
lista2.append("blá")
print(lista2)

print(lista[3:])

lista.extend(lista2)
print(lista)
print(len(lista))

if True in lista:
    print("Tem True sim")

del lista[2:]
print(lista)

lista.insert(0,8)
print(lista)

print(lista.index("qualquer"))
lista.reverse()
print(lista)

lista.remove(8)
print(lista)

lista.append("ali")
print(lista)

lista.sort()
print(lista)

lista.clear()
print(lista)


lista_num = [3,6,7,34,89,123,64,123,876,123,99,79,596,7]
lista_num.sort(reverse=True)
print(lista_num)

lista_num = [3,6,7,34,89,123,64,123,876,123,99,79,596,7]
lista_num = sorted(lista_num)
print(lista_num)

lista_num = [3,6,7,34,89,123,64,123,876,123,99,79,596,7]
lista_num.reverse()
print(lista_num)


lista_em_dobro = [1,2,3,4,5] * 2

print(lista_em_dobro)