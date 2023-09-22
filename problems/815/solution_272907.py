def insere(lista_numero,n):
    '''Dada uma lista ordenada(crescente) de números inteiros e um número inteiro n, inclui n na posição correta, de maneira que a lista continue ordenada.
    :param lista_numero: list
    :param n: int'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero