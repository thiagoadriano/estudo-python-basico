lista = ["gato", "cachorro", "papagaio", "piriquito", "hamster"]

for idx in range(len(lista)):
    print(idx, lista[idx])

for idx, animal in enumerate(lista):
    print(idx, animal)

enum = dict(enumerate(lista))
print(enum)
dictEnum = {}


for key in enum:
    dictEnum[key] = enum[key];
    dictEnum[enum[key]] = key;

print(dictEnum)

print(dictEnum['gato'])
print(dictEnum[0])