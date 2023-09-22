def eh_quadrada(matriz):
    """A função booleana recebe como entrada uma matriz e avalia
    se esta é quadrada ou não;
    list(list) -> bool"""
    if matriz == [] or len(matriz) == len(matriz[0]):
        return True
    else:
        return False