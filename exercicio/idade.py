idade = input("Informe a sua idade: ")

if not idade.isdigit(): 
    print("Informe somente números")
else:
    idade = float(idade)
    if idade < 18:
        print("Sua idade é menor que o esperado")
    else:
        print("Você é maior de idade")