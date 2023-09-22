def total(x,y):
    """ Recebe uma lista de compras e um dicionário contendo o preço
    de cada produto disponível em uma loja, e retorna o valor total
    dos itens da lista que estejam disponíveis nesta loja.
    assinatura: list, dict--> float
    """
    s = 0
    for c in range(len(x)):
        s = s + y[x[c]]
    return round(s,2)