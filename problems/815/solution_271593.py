def insere(lista_numero, n):
    """Recebe uma lista ordenada e um número, e retorna
    uma lista com o número em seu devido lugar.
    list, int -> list"""
    lista_numero.append(n)
    return lista_numero.sort()