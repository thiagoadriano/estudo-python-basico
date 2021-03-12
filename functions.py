def fn_teste(valor):
    print(valor)
    return "Pode ser outro também"

def fn_rec(valor, limite):
    if valor < limite:
        print(valor)
        valor += 1
        fn_rec(valor, limite)
    else:
        print('Concluído')

print(fn_teste("Novo valor"))

fn_rec(0, 50)