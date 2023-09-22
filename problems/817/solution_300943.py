def acima_da_media(lista_numeros):
    ''' função que retorna uma lista com a ordem das notas de quem foi acima da média.
    list(int) -> list
    '''
    soma = sum(lista_numeros)
    n = len(lista_numeros)
    media=(soma//n)
    list.append(lista_numeros, media)
    list.sort(lista_numeros)
    lista1 = lista_numeros[list.index(lista_numeros, media) + 1:]
    return lista1