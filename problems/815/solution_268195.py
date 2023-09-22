def insere(list_numero, n):
    """dada uma lista ordenada (crescente) de n ́umeros inteiros e um n ́umero inteiro n, função inclui n na posição correta, ou seja,
       de tal maneira que a lista continue ordenada."""
    """ lista -> lista"""
    lista = list_numero
    list.insert(lista, 2, n)
    lista.sort()
    return lista