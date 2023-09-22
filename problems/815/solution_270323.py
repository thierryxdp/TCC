def insere(lista_numero,n):
    """função que, dados uma lista ordenada de números inteiros e um número
    inteiro n, inclui n nessa lista de forma que a mesma continue ordenada.
    list, int -> list"""
    lista_atual = lista_numero + [n]
    lista_atual.sort()

    return lista_atual