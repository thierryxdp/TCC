def filtra_pares(x):
    """Dado uma tupla com 4 elementos de inteiros, retorna somente os pares
    assinatura: tuple (int, int, int, int) -> tuple
    testes:
    filtra_pares(2, 4, 6, 8) == (2, 4, 6, 8)
    filtra_pares(2, 4, 6, 9) == (2, 4, 6)
    filtra_pares(2, 4, 7, 9) == (2, 4)
    filtra_pares(2, 5, 7, 9) == (2)
    filtra_pares(3, 5, 7, 9) == ()
    """
    ret = ()
    if x[0] % 2 == 0:
        ret = ret += (x[0],)
    if x[1] % 2 == 0:
        ret = ret += (x[1],)
    if x[2] % 2 == 0:
        ret = ret += (x[2],)
    if x[3] % 2 == 0:
        ret = ret += (x[3],)
    return ret