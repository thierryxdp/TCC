def total(l,d):
    """Dada uma lista de compras "l" e um dicionário "d"
    contendo o preço de cada produto disponível, retorna
    o valor total dos itens disponíveis
    list , dict -> float"""
    for l in d:
        if l in d:
            soma += d[l]
        else:
            return 0
    return soma