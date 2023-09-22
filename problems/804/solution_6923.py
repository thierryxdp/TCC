def filtra_pares(x1,x2,x3,x4):
	"""funçao que recebe uma tupla com quatro elementos inteiros como
    parametro e retorna uma nova tupla contendo apenas os elementos
    pares da tupla original na mesma ordem em que se encontravam;
    tupla(int,int,int,int) -> tupla(int)
    """
    if x1 % 2 == 0 and x2 % 2 == 0 and x3 % 2 == 0 and x4 % 2 == 0:
        return x1, x2, x3, x4

    if x1 % 2 != 0 and x2 % 2 == 0 and x3 % 2 == 0 and x4 % 2 == 0:
        return x2, x3, x4
    if x1 % 2 != 0 and x2 % 2 != 0 and x3 % 2 == 0 and x4 % 2 == 0:
        return x3, x4
    if x1 % 2 != 0 and x2 % 2 != 0 and x3 % 2 != 0 and x4 % 2 == 0:
        return x4

    if x1 % 2 == 0 and x2 % 2 != 0 and x3 % 2 == 0 and x4 % 2 == 0:
        return x1, x3, x4
    if x1 % 2 == 0 and x2 % 2 != 0 and x3 % 2 != 0 and x4 % 2 == 0:
        return x1, x4
    if x1 % 2 == 0 and x2 % 2 != 0 and x3 % 2 != 0 and x4 % 2 != 0:
        return x1

    if x1 % 2 == 0 and x2 % 2 == 0 and x3 % 2 != 0 and x4 % 2 == 0:
        return x1, x2, x4
    if x1 % 2 == 0 and x2 % 2 == 0 and x3 % 2 != 0 and x4 % 2 != 0:
        return x1, x2

    if x1 % 2 == 0 and x2 % 2 == 0 and x3 % 2 == 0 and x4 % 2 != 0:
        return x1, x2, x3

    if x1 % 2 != 0 and x2 % 2 == 0 and x3 % 2 != 0 and x4 % 2 == 0:
        return x2, x4
    if x1 % 2 == 0 and x2 % 2 != 0 and x3 % 2 == 0 and x4 % 2 != 0:
        return x1, x3
    if x1 % 2 != 0 and x2 % 2 == 0 and x3 % 2 == 0 and x4 % 2 != 0:
        return x2, x3

    if x1 % 2 != 0 and x2 % 2 != 0 and x3 % 2 != 0 and x4 % 2 != 0:
        return ()