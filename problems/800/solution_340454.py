def total(compras, precos):
    '''Recebe uma lista de compras e um dicionário contendo
    o preço de cada produto disponível em uma loja, e retorna
    o valor do total dos itens da lista disponíveis na loja
    list, dict -> float'''
    valor = 0
    for i in range(0, len(compras) + 1):
        if compras[i] in produtos:
            valor += precos[compras[i]]
    return valor