def pares(item):
    if item % 2 == 0:
        return item
    else:
        pass

lista = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

valores = filter(pares, lista)

print(list(valores))