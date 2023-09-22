def acima_da_média(lista):
    '''Dada uma lista de números inteiros retorna uma lista 
    com os números maiores que a média.
    list -> list'''
    media = lista.sum()
    lista.append(media)
    lista.sort()
    return lista[lista.index(n) + 1:]