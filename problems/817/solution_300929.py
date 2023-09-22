def acima_da_media(lista_numeros):
    ''' função que retorna uma lista com a ordem das notas de quem foi acima da média.
    list(int) -> list
    '''
    list.insert(lista_numeros, 0, n)
    list.sort(lista_numeros)
    lista1 = lista_numeros[list.index(lista_numeros, n) + 1:]
    media = int(sum(lista_numeros) // len(lista_numeros))
    return lista1