def total(lista=[], dicionario={}):
    """Recebe uma lista de compras e um dicionario e retorna
    o valor total dos itens da lista, que estão disponiveis"""
    c = 0.0
    
    for i in lista:
        c += dicionario[i]
    return round(c,2)