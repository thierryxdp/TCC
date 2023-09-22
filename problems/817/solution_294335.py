def acima_da_media(lista):
    '''Funcao que retorna uma lista com todas as notas acima da media.
list->list'''
    media=sum(lista)//len(lista)
    list.sort(lista)
    y=list.index(lista,media)
    return lista[y+1:]