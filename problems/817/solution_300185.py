def acima_da_media(lista):
    '''Função que retorna as notas que ficaram acima da média.
    list->list'''
    import math
    x= list.sort(lista)
    media= math.ceil(sum(x)/len(lista))
    a= list.index(x,media)
    del lista[:a]
    return lista