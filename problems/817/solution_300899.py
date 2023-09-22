def acima_da_media(lista_nota):
    ''' função que retorna uma lista com a ordem das notas de quem foi acima da média.
    list(int) -> list
    '''
    soma = sum(lista_nota)
    n = len(lista_nota)
    media = (soma//n)
    list.insert(lista_nota, 0, media)
    list.sort(lista_nota)
    lista1 = lista_nota[list.index(lista_nota, media) + 1:]
    list.sort(lista1)
    return lista1