def insere(lista_numero, n):
    """ Dada uma lista ordenada (crescente) de números inteiros e um número inteiro n, inclui n na posição correta, de tal maneira que a lista continue ordenada
    list, int -> list """
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero