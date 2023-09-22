def total(compras, precos):
    '''Recebe uma lista de compras e um dicionário com os
    preços de cada produto e retorna o valor total dos itens
    da lista de entrada
    list, dict -> float'''
    total = 0
    for item in compras:
        total += precos[item]
    return round(total,2)