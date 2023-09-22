def colchao( medidas, H, L):
    """
    Dados tres dimensoes de um colchao em centimetros, verifica se 
    :param H: int -> int
    :param L: int -> int
    :return: bool -> boo"""
    [ A, B, C] = medidas
    if A and B > H and L :
        return False
    else:
        return True