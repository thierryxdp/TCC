def repetidos(l):
    """Recebe como parâmetro uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior;
    assinatura: list(...) --> int
    Casos de teste:
    repetidos([1, 4, 3, 3, 2, 3, 3, 3, 3, 5, 4, 6, 6, 7, 6, 8, 8, 7]) == 6
    repetidos([1, 1, 1, 1]) == 3
    repetidos([0, 0, 3, 3, 4, 4, 0]) == 3
    """
    z = 0
    for i, e in enumerate(l):
        if i != 0:
            if e == l[(i -1)]:
                z += 1
    return z