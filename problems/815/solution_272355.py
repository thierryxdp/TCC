def insere(lista_numero, n):
    """funcao que insere um numero n na lista ordenada, de modo que a lista continue em ordem crescente.
    int, int -> int"""
    lista_numero.append(n)
    lista_numero.sort()
    return lista_numero