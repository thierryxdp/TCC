def eh_quadrada(matriz):
    """Função que verifica se uma matriz é quadrada. list -> bool"""
    if len(matriz) == 0:
        return True
    for m in range(len(matriz)):
        while m < len(matriz):
            if len(matriz[m]) == len(matriz):
                m += 1
            else:
                return False
        return True