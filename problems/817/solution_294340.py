def acima_da_media(lista):
    '''Função que retorna uma lista ordenada com as notas que
    ficaram acima da média
    lista=list->list'''
    x = sum(lista)
    list.sort(lista)
    z = list.index(lista,x)
    return lista[z:]