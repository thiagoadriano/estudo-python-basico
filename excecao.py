a = 2
b = 0
c = "2"
d = [2,3]



try: 
    print(a/b)

except:
    print("Erro na divisão")

try:
    print(a/c)

except TypeError as error:
    print(error)

try:
    print(a/b)
    print(a/c)
    print(2 / d[2])

except TypeError as error:
    print("Erro generalizado: ", error)

except ZeroDivisionError as divider:
    print("Erro de divisao: ", divider)

except IndexError as index:
    print("Erro de indexação: ", index)

except:
    print("Erro sem tratamento específico!")

finally:
    print("Execução independente!")