def total(l,d):
    '''Essa função ao receber uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, ela retornara o valor total dos itens'''
    '''list,dic -> float'''
    v = []
    for i in l:
        if i in d:
            list.append(v, dict.get(d,i))
    return round(sum(v),2)