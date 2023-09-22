def acima_da_media(lista):
    '''retorna uma lista das notas que ficaram acima da média. list->list'''
    media=sum(lista)/len(lista)
    if media in lista==False:
        list.append(lista,media)
        list.sort(lista)
        del lista[:1+list.index(lista,media)]
        return lista
    if media in lista==True:
        list.append(lista,media)
        list.sort(lista)
        del lista[:list.index(lista,media)]
        return lista