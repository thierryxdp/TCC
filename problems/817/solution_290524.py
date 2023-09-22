def acima_da_media(lista):
    '''retorna uma lista das notas que ficaram acima da média. list->list'''
    list.append(lista,sum(lista)/len(lista))
    list.sort(lista)
    del lista[:list.index(lista,sum(lista)/len(lista))+1)
    return lista