def total(lista, preco):
    soma = 0
    for x in lista:
        soma = soma + precos[x]
    return round(soma, 2)