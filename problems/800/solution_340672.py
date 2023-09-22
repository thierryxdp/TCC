def total(lista, produtos):
    soma = 0.00
    i = 0
    while i < len(lista):
        a = produtos[lista[i]]
        soma = soma + a
        i = i + 1
    round (soma,2)
    return float(soma)