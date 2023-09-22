def colchao( medidas, H, L):
    """
    Dados tres dimensoes de um colchao em centimetros, verifica se 
    :param H: int -> int
    :param L: int -> int
    :return: bool -> boo"""
    [ A, B, C] = medidas
    if B > L:
        return False
    if C > H:
        return False
    else:
		return True