def total(lista, produtos):
    soma = 0
    i = 0
    while i < len(lista):
        a = produtos[lista[i]]
        soma = soma + a//1
        i = i + 1
    return soma