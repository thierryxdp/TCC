def eh_quadrada(matriz):
    """
    Verifica se uma matriz é quadrada, isto é, verifica se ela contém nenhuma linha e nenhuma coluna.
    :return: bool -> bool
    """

    if len(matriz) == 0:
        return True

    for lin in range(0, len(matriz)):
        if len(matriz[lin]) == 0:
            return True

        for col in range(0, len(matriz[lin])):
            if matriz[lin] == matriz[lin][col] or len(matriz[lin]) == len(matriz[col]):
                return True

            else:
                return False