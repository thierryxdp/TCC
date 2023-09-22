def maiores(lista: list, n: int) -> list:
    '''
    Retorna lista com os números maiores que n, dado a lista de números e o n que vai ser comparado
    '''
    lista.append(n)
    list.sort(lista)
    a = lista.index(n)
    return lista[:a]