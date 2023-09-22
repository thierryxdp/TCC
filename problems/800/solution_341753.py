def total (lista, produtos):
    """dada uma lista de compras e um dicionario contendo produtos e seus valores, retorna o valor total dos itens da lista disponiveis;
    list,dict->float"""
    d=0
    c=0
    while d<len(lista):
        c+=produtos[lista[d]]
        d+=1
    return round(c,2)