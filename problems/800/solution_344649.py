def total(lista, preco):
    soma = 0
    for x in lista:
        soma = soma + preco[x]
    return round(soma, 2)