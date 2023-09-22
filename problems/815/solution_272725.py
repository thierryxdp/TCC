def insere(listaNumeroOrdenada: list[int], n: int) -> list[int]:
    '''Insere n na sua respectiva posicao dentro da lista
       de numeros ordenada'''
    listaNumeroOrdenada.append(n)
    listaNumeroOrdenada.sort()

    return listaNumeroOrdenada