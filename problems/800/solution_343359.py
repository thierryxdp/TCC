def total(compras, precos):
    '''retorna o valor total dos itens disponíveis na lista de compras, a partir do dicionário dado com os seus preços
    list, dict -> float'''
    total = 0
    for item in compras:
        total += dict.get(precos, item, 0)
    return total