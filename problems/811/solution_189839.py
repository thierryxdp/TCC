def colchao(medidas, H, L):
    """
    funcao definida por tres parametros, medidas, H (altura) e 
    L (largura) calculados em centimetros, e retorna se o
    colchao passa pela porta
    :param medidas: list (medidas do colchao)
    :param H: int (medida da porta)
    :param L: int (medida da porta)
    :return: bool
    """
    [A, B, C] = medidas
    if A and B > H and L:
        return False

    else:
        return True