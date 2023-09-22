def total(lista,preco):
    soma = 0
    i = 0
    for elem in preco:
        if elem in preco:
            soma = soma + preco[elem]
            i = i+1
    return round(soma,2)