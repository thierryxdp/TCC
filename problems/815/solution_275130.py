def insere(lista_numero, n):
    """Dada uma lista e um número n, adiciona n na lista e coloca em ordem crescente
    assinatura:
    tupla (list, int) -> list
    testes:
    insere ([1, 2, 3, 4, 6], 5) == [1, 2, 3, 4, 5, 6]
    insere ([1, 2, 3, 4, 7, 10], 6) == [1, 2, 3, 4, 6, 7, 10]
    """
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero