def acima_da_media(lista):
    '''Retorna os numeros acima da media
    lista->lista'''
    media = (sum(lista) // len(lista)) + 0.1
    lista.append(media)
    lista.sort()
    lista = lista[lista.index(media) + 1 : ]
    return lista