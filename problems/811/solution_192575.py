def colchao(medidas, H, L):
    """Dado três dimensões de um colchão em centímetro, verifica se esse colchão passa pela porta de altura H e largura L.
    list -> list
    H: int -> int
    L: int -> int
    return: bool -> bool"""
    [A, B, C] = medidas
    if A > L and C > H:
        return False
    else:
        return True