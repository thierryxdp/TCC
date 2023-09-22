def acima_da_media(lista):
    '''retorna uma lista com as notas acima da media; list -> list'''
    media = sum(f)/len(f)
    a = list.sort(lista)
    b = list.index(lista, media)
    lista = lista[media:]