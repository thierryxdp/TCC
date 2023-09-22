def insere(lista_numero, n):
    """Recebe uma lista de números inteiros ordenada e um
número inteiro n. Retorna uma nova lista ordenada com n
inserido nessa lista.
list, int -> list
"""
    lista_completa = lista_numero + [n]
    list.sort(lista_completa)
    return lista_completa