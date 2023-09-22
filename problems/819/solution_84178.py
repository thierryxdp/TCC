def filtraMultiplos(l, n):
    """Recebe como parâmetro uma lista de números l e um número n e retorna uma nova lista contendo todos os elementos da lista original que são divisíveis por n;
    assinatura: list(...), float --> list(...)
    Casos de teste:
    filtraMultiplos([1, 2, 3, 4, 5, 6], 2) == [2, 4, 6]
    filtraMultiplos([1, 2, 3, 4, 5, 6], 3) == [3, 6]
    filtraMultiplos([1, 2, 3, 4, 5, 6], 1) == [1, 2, 3, 4, 5, 6]
    filtraMultiplos([1, 2, 3, 4, 5, 6, -1, -2, -3, -4, -5, -6], 6) == [6, -6]
    """
    lista_aux = []
    for e in l:
        if (e % n) == 0:
            lista_aux.append(e)
    return lista_aux