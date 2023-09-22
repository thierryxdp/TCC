def acima_da_media(lista_nota):
    ''' função que retorna uma lista com a ordem das notas de quem foi acima da média.
    list(int) -> list
    '''
    media=int(sum(lista_nota) / len(lista_nota)
    list.insert(lista_nota, 0, media)
    list.sort(lista_nota)
    lista1 = lista_nota[list.index(lista_nota, media) + 1:]
    return lista1