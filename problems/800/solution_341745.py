def total (lista):
    '''valor total dos itens da lista'''
    lista = str.split(lista,' ')
    dicio = {}
    for x in lista:
        dicio[x] = list.count(lista,x)
    return round(dicio, 2)