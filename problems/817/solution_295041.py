def maiores(listnum: list, n: float) -> list:    
    '''Dada uma lista de inteiros e um inteiro n, devolve
    lista com os inteiros maiores que n contidos na lista
    fornecida'''
    list.append(listnum, n)
    list.sort(listnum)
    lista = listnum[(list.index(listnum, n) + 1) :]
    return lista


def acima_da_media(notas: list) -> list:
    '''Dada uma lista de notas, devolve aquelas que foram
    acima da média'''
    media = sum(notas) / len(notas)
    return maiores(notas, media)