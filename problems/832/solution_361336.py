def eh_quadrada(matriz):
    "Indentifica se uma matriz é quadrada; list -> bool"
    if len(matriz) == 0:
        return True
    elif len(matriz) == len(matriz[0]):
        return True
    else:
        return False