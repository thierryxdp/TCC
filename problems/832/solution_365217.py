def eh_quadrada(matriz):
    """Essa função analiza se uma matriz e quadrada 
    list -> bool"""
    if len(matriz) == 0:
        return True
    for i in range(len(matriz)):
        while i < len(matriz):
            if len(matriz[i]) == len(matriz):
                i += 1
            else:
                return False
        return True