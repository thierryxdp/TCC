def insere(lista_numero, n):
    """Função que dado uma lista(lista_numero) ordenada, crescente, de um número
    de inteiros e um número inteiro(n), inclua 'n' na posição correta.
    lista, int -> lista"""

    lista_numero[0:0] = n
    list.sort(lista_numero)
    return lista_numero