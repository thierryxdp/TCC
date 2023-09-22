def eh_quadrada(matriz):
    """
    Verifica se uma matriz é quadrada, isto é, verifica se ela contém nenhuma linha e nenhuma coluna.
    :return: bool -> bool
    """
    for lin in range(0, len(matriz)):
        if len(matriz[lin]) == 0:
            return True

        for col in range(0, len(matriz[lin])):
            if matriz[lin] == matriz[lin][col]:
                return True

            else:
                if matriz[col] == matriz[lin]:
                    return True
                else:
                    return False