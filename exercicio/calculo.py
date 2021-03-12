print("""
######
 Esse programa tira a média de dois números inteiros
###
""")
num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")

if not num1.isdigit() or not num2.isdigit():
    print("Ambos valores precisam ser números")
else:
    num1 = int(num1)
    num2 = int(num2)
    resultado = (num1 + num2) / 2
    print("O resultado é: ", int(resultado))