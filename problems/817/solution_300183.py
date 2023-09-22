def acima_da_media(lista):
    '''Função que retorna as notas que ficaram acima da média.
    list->list'''
    import math
    media= math.ceil(sum(lista)/len(lista))
    a= list.index(lista,media)
    del lista[a:]
    return lista