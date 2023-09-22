def colchao(medidas,H,L):
    """Determina se um colcão com dimensões contidas na lista
    'medidas' pode passar uma porta de altura H e largura L;
    list, int, int -> bool"""
    if medidas[0] and medidas[1] <= H or <= L:
        return True
    elif medidas[0] and medidas[2] <= H or <= L:
        return True
    elif medidas[1] and medidas[2] <= H or <= L:
        return True
    else:
        return False