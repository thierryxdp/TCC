def maiores(lista, n):
    '''Retorna uma lista com os números maiores que o n dado. List, Int -> List'''
    list.insert(lista, 1, n)
    list.sort(lista)
    Posicao_n = list.index(lista, n)
    NovaLista = lista[Posicao_n + 1:]
    return NovaLista