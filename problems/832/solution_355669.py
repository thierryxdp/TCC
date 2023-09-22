def eh_quadrada(matriz):
    """dada uma matriz no formato lista de listas, a função retorna True se ela for quadrada e False, caso não;
    list -> bool"""
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False