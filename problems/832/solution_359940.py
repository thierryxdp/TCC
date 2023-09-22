def eh_quadrada(matriz):
    """Identifica se uma matriz é quadrada ou não
    input: matriz -> list
    output: boolean 
    """
    if matriz == []:
        return True
    else:
        return True if len(matriz) == len(matriz[0]) else False