def eh_quadrada(matriz):
    """Recebe uma matriz e verifica se é quadrada. Retorna True se é quadrada e
    False caso contrário
    list -> bool"""
    if len(matriz[0]) == len(matriz):
        return True
    elif matriz == []:
        return True
    else:
        return False