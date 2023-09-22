def colchao(medidas, H, L):
    """
    :param medidas: list 
    :param H: int 
    :param L: int
    :return: bool 
    """
    [A, B, C] = medidas
    if B and C > H and L:
        return False
    elif B and C < H and L:
        return True