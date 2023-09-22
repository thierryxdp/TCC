def total(lista,preco):
    soma = 0
    for elem in lista:
        if elem in preco:
            soma = soma + preco[elem]
    return round(soma,2)