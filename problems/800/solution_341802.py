def total(lista,preco):
    soma = 0
    for elem in preco:
        if preco in lista[elem]:
            soma = soma + [elem]
    return soma