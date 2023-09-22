def eh_quadrada (matriz):
    """Se uma matriz é quadrada, retorna True...Se não, False
    Entrada: list(list)
    Saída: bool
    """
    if len(matriz) > 0:
        if len(matriz) == len(matriz[0]):
            return True
        else:
            retuurn False
    else:
        return True