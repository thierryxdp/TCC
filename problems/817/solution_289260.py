def acima_da_media(lista):
    '''Dada uma lista de números inteiros retorna uma lista 
    com os números maiores que a média.
    list -> list'''
    media = sum(lista)/len(lista)
    lista.append(media)
    lista.sort()
    return lista[lista.index(media) + 1:]