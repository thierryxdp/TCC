def total(compras,preco):
    """recebe uma lista de compras e um dicionário contendo o preço de cada produto e 
    retorna o valor total dos itens da lista.
    list,dict->float"""
    p=0
    for i in range(len(compras)):
        p=p+preco[compras[i]]
    return round(p,2)