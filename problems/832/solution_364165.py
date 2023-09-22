def eh_quadrada(matriz):
    """Função booleana que identifica se uma matriz é
    quadrada.(Uma matriz vazia é considerada quadrada)
    list -> bool"""
    if len(matriz) == 0 and len(matriz[0]) == 0:
        return True
    else:
        return False