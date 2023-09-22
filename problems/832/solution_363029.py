def eh_quadrada(matriz:list)->bool:
    """identifica se a matriz é quadrada"""
    if matriz != []:
       return len(matriz) == len(matriz[0])
    else:
        True