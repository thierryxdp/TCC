def total(lista, produtos):
    soma = 0.00
    i = 0
    while i < len(lista):
        a = produtos[lista[i]]
        soma = soma + float(a)
        i = i + 1
    return soma