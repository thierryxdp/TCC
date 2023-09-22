def total(lista, produtos):
    soma = 0.0
    i = 0
    while i < len(lista):
        a = produtos[lista[i]]
        soma = soma + a
        i = i + 1
    print soma