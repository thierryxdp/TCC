def acima_da_media(lista):
    '''retorna uma lista com as notas acima da media; list -> list'''
    media = sum(lista)/len(lista)
    b = list.append(lista, media)
    return lista