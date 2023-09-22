def colchao(medidas,H,L):
    """
    Dado três dimensões de um colchão em centímetro, verifica se esse colchão passa pela porta de altura H e largura L.
    list, int, int -> bool
    """
    if medidas[1]<=L and medidas[2]<=H:
        return True
    if medidas[0]<=L and medidas[1]<=H:
        return True
    if medidas[0]<=L and medidas[2]<=H:
        return True
    else:
        return False