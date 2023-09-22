def insere(listaNumeroOrdenada: list[int], n: int) -> list[int]:
    '''recebe uma lista ordenada de numeros inteiros e um numero inteiro 'n'
    e inclui esse numero de forma ordenada'''
    listaNumeroOrdenada.append(n)
    listaNumeroOrdenada.sort()

    return listaNumeroOrdenada