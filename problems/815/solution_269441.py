def insere (lista_numero, n):
    """Recebe uma lista em ordem crescente e um número, e os
    retorna em ordem crescente.
    list, int -> list"""
    nlista = lista_numero + ((n,))
    return list.sort(nlista)