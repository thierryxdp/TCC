def filtra_pares(tupla):
    """funçao que recebe uma tupla com quatro elementos inteiros como
    parametro e retorna uma nova tupla contendo apenas os elementos
    pares da tupla original na mesma ordem que se encontravam;
    tupla(int,int,int,int) -> tupla
    """

    if tupla[0] % 2 == 0 and tupla[1] % 2 == 0 and tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
        return tuple(tupla)

    if tupla[0] % 2 != 0 and tupla[1] % 2 == 0 and tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
        return tuple(tupla[1:])
    if tupla[0] % 2 != 0 and tupla[1] % 2 != 0 and tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
        return tuple(tupla[2:])
    if tupla[0] % 2 != 0 and tupla[1] % 2 != 0 and tupla[2] % 2 != 0 and tupla[3] % 2 == 0:
        return tupla[3],

    if tupla[0] % 2 == 0 and tupla[1] % 2 != 0 and tupla[2] % 2 == 0 and tupla[3] % 2 == 0:
        return tupla[0], tupla[2], tupla[3]
    if tupla[0] % 2 == 0 and tupla[1] % 2 != 0 and tupla[2] % 2 != 0 and tupla[3] % 2 == 0:
        return tupla[0], tupla[3]
    if tupla[0] % 2 == 0 and tupla[1] % 2 != 0 and tupla[2] % 2 != 0 and tupla[3] % 2 != 0:
        return tupla[0],

    if tupla[0] % 2 == 0 and tupla[1] % 2 == 0 and tupla[2] % 2 != 0 and tupla[3] % 2 == 0:
        return tupla[0], tupla[1], tupla[3]
    if tupla[0] % 2 == 0 and tupla[1] % 2 == 0 and tupla[2] % 2 != 0 and tupla[3] % 2 != 0:
        return tuple(tupla[0], tupla[1])

    if tupla[0] % 2 == 0 and tupla[1] % 2 == 0 and tupla[2] % 2 == 0 and tupla[3] % 2 != 0:
        return tuple(tupla[0], tupla[1], tupla[2])

    if tupla[0] % 2 != 0 and tupla[1] % 2 == 0 and tupla[2] % 2 != 0 and tupla[3] % 2 == 0:
        return tuple(tupla[1], tupla[3])
    if tupla[0] % 2 == 0 and tupla[1] % 2 != 0 and tupla[2] % 2 == 0 and tupla[3] % 2 != 0:
        return tuple(tupla[0], tupla[2])
    if tupla[0] % 2 != 0 and tupla[1] % 2 == 0 and tupla[2] % 2 == 0 and tupla[3] % 2 != 0:
        return tuple(tupla[1], tupla[2])

    if tupla[0] % 2 != 0 and tupla[1] % 2 != 0 and tupla[2] % 2 != 0 and tupla[3] % 2 != 0:
        return ()