arquivo = open("texto.txt")

print(arquivo.readline())
print(arquivo.readline())
print(arquivo.readline())

texto_completo = arquivo.read()
print(texto_completo)

linhas = arquivo.readlines()
for linha in linhas:
    print(linha)

print(arquivo.closed)
arquivo.close()
print(arquivo.closed)
