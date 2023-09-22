def acima_da_media(lista):
    '''Funcao que retorna uma lista com todas as notas acima da media.
list->list'''
    media=sum(lista)
    return maiores(lista,media)