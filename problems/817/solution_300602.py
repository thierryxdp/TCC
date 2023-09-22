def acima_da_media(lista):
    '''Função que dada uma lista, retorna uma lista ordenada contendo somente as notas que ficaram
    acima da média; list->list'''
    
    soma_notas=sum(lista)
    media=soma_notas/(len(lista))
    lista=lista+[media]
    list.sort(lista)
    x=lista.index(media)
    lista=lista[x:]
    list.remove(lista,media)
    if media==lista[0]:
        return[]
    else:
        return lista