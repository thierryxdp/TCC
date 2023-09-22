def maiores(listnum: list, n: int) -> list:
    '''Dada uma lista de inteiros e um inteiro n, devolve
    lista com os inteiros maiores que n contidos na lista
    fornecida'''
    list.append(listnum, n)
    list.sort(listnum)
    lista = listnum[(list.index(n) + 1) :]
    return lista