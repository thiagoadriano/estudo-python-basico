def dobro(val):
    return val * 2

lista = [1,2,3,4,5,6,7,8]

print(list(map(dobro,lista)))

dobroMap = map(lambda val: val * 2, lista)

print(list(dobroMap))