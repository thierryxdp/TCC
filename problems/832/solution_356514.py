def eh_quadrada(matriz):
    """
    Verifica se uma matriz é quadrada, isto é, verifica se ela contém nenhuma linha e nenhuma coluna.
    :return: bool -> bool
    """
    for lin in range(0, len(matriz)):
        for col in range(0, len(matriz[lin])):
            if matriz[lin] == matriz[lin][col]:
                return True

            if matriz[lin][col] == 0:
                return True

            else:
                return False