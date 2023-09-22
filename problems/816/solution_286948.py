def maiores (lista, n):
    """Dada uma lista e um inteiro n, retorna a lista com os números maiores que n
    assinatura:
    tuple (list, int) -> list
    testes:
    maiores ([1, 2, 3, 4, 5], 2) == [3, 4, 5]
    maiores ([1, 2, 3, 4, 5, 6, 7], 6) == [7]
    maiores ([3, 4, 5], 5) == []
    """
	if n > lista[:]:
        return 
    list.sort (lista)
    return lista