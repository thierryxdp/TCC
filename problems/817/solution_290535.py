def acima_da_media(lista):
    '''retorna uma lista das notas que ficaram acima da média. list->list'''
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    del lista[:list.index(lista,media)]
    return lista