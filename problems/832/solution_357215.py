def eh_quadrada(matriz):
    """Recebe uma matriz e verifica se é quadrada. Retorna True se é quadrada e
    False caso contrário
    list -> bool"""
    if matriz == []:
        return True
    elif len(matriz[0]) == len(matriz):
        return True
    else:
        return False