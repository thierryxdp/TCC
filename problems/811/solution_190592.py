def colchao(medidas, H, L):
    """
    Dado três dimensões de um colchão em centímetro, verifica
    se esse colchao passa pela porta de altura H e largura L.
    :param medidas: list 
    :param H: int 
    :param L: int
    :return: bool 
    """
    [A, B, C] = medidas
    if A and B > H and L:
        return False
    else:
        return True