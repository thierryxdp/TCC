def acima_da_media(lista):
    """funcao que retorna os numeros de uma lista dada maior que de uma determinada media;lista->lista"""
    list.sort(lista)
    media=(len(lista)//2)
    return lista[(media+1):]