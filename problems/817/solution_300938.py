def acima_da_media(lista_numeros):
    ''' função que retorna uma lista com a ordem das notas de quem foi acima da média.
    list(int) -> list
    '''
    soma = sum(lista_numeros)
    n = len(lista_numeros)
    media=(soma/n)
    list.insert(lista_numeros, 0, media)
    list.sort(lista_numeros)
    lista1 = lista_numeros[list.index(lista_numeros, media) + 1:]
    list.sort(lista1)
    return lista1