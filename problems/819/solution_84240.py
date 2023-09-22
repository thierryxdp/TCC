def filtraMultiplos(ls, n):
    """Dado uma lista com k inteiros e um número n, retorna outra lista com k inteiros que forem divisíveis por n
    assinatura: list -> list
    testes:
    filtra_multiplos ([2, 4, 6, 8], 2) == [2, 4, 6, 8]
    filtra_multiplos ([2, 4, 6, 8], 3) == []
    """
    lista = []
    for i in ls:
        if i % n == 0:
            lista.append (i)
    return lista