def total(lista,preco):
    soma = 0
    for elem in preco:
        if lista in preco[elem]:
            soma = soma + [elem]
    return soma