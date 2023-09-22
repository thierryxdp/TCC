def acima_da_media(lista):
    '''Calcula a média das notas da lista e retorna uma nova lista com as notas acima da média ordenadas'''
    '''list -> list'''
    media=sum(lista)/len(lista)
    list.append(lista,media)
    list.sort(lista)
    posição=list.index(lista,media)
    del lista[:posição]
    return lista