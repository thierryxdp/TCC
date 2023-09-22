def acima_da_media(lista):
    '''Calcula a média das notas da lista e retorna uma nova lista com as notas acima da média ordenadas'''
    '''list -> list'''
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    posicao=list.index(lista,media)
    del lista[:posicao+1]
    if media in lista:
        list.remove(lista,media)
        return lista
    else:
        return lista