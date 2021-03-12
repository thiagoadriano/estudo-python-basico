base = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
exponenciacao = [n ** 2 for n in base]
numeros_pares = [n for n in base if n % 2 == 0]
numeros_impares = [n for n in base if n % 2 == 1]

print(exponenciacao, "Total de registros: ", len(exponenciacao))
print(numeros_pares, "Total de registros: ", len(numeros_pares))
print(numeros_impares, "Total de registros: ", len(numeros_impares))