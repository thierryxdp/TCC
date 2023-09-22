def colchao(medidas, H, L):
    """
    :param medidas: list 
    :param H: int 
    :param L: int
    :return: bool 
    """
    [A, B, C] = medidas
    if A and B > H and L:
        return False
    elif A and B < H and L:
        return True