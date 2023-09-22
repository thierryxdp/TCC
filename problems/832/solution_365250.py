def eh_quadrada(matriz):
    """Essa função identifica se uma matriz e quadrada ou não
    list -> bool"""
    if len(matriz) == 0:
        return True
    for x in range(len(matriz)):
        while x < len(matriz):
            if len(matriz[x]) == len(matriz):
                x += 1
            else:
                return False
        return True