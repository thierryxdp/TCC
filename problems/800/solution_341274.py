def total(l,d):
    '''Essa função ao receber uma lista de compras e um dicionário contendo o preço de cada produto disponível em uma determinada loja, ela retornara o valor total dos itens'''
    '''list,dic -> float'''
    valor = []
    for i in l:
        if i in d:
            list.append(valor, dict.get(d,i))
    return round(sum(valor),2)