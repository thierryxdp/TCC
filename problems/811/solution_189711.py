def colchao(medidas, H, L):
"""Dado três dimensões de um colchão em centímetros, verifica se esse colchão passa pela porta de altura H e largura L.
    list, int, int -> bool"""
    if medidas[0] and medidas[1] > H and L:
        return False

    else:
        return True