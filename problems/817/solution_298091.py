def acima_da_media(lista):
    """ dado uma lista de entrada,calcula a media da lista e retorna apenas os termos acima da media
    list--> list"""
    x = lista
    a = sum(x)
    b = len(x)
    c = a/b
    list.insert(x, -1, c)
    a = sorted(x)
    b = list.index(a, c)
    del a[:b + list.count(a,c):1]
    return a