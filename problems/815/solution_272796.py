def insere (lista_numero, n):
    """Funcao que dada uma lista ordenada de números inteiros e um inteiro 'n', inclua 'n' na posição correta e a lista continue ordenada"""
    """lista, int -> lista"""
    list.append (lista_numero, n)
    list.sort (lista_numero)
    return lista_numero