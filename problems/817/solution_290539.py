def acima_da_media(lista):
    '''retorna uma lista das notas que ficaram acima da média. list->list'''
    media=sum(lista)/len(lista)
    if int(media) in lista==True:
        list.sort(lista)
        del lista[:1+list.index(lista,int(media))]
        return lista
    else:
        list.append(lista,media)
        list.sort(lista)
        del lista[:1+list.index(lista,media)]
        return lista