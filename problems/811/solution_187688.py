def colchao(medidas, h, l):
    """ Dado três dimensões de um colchão em centímetro, verifica se esse colchão passa pela porta de altura H e largura L."""
    [A, B, C] = medidas
    if A and B > h and l:
        return false
    else:
        return true