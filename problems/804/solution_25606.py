def filtra_pares(x):
    """Retorna somente os pares de uma tupla com quatro elementos.
    Assinatura: tuple (int, int, int, int) -> tuple
    Casos de teste:
    filtra_pares(2, 4, 6, 8) == (2, 4, 6, 8)
    filtra_pares(2, 4, 5, 6) == (2, 4, 6)
    filtra_pares(2, 4, 5, 9) == (2, 4)
    filtra_pares(2, 3, 5, 7) == (2)
    filtra_pares(3, 5, 7, 9) == ()
    """
    ret = ()
    if x[0]%2 == 0:
        ret += (x[0],)
    if x[1]%2 == 0:
        ret += (x[1],)
    if x[2]%2 == 0:
        ret += (x[2],)
    if x[3]%2 == 0:
        ret += (x[3],)
    return ret