def colchao(medidas, H, L):
    """list, int, int -> bool"""
    if medidas[1] < H:
        if medidas[1] <= L:
            return True
        else:
            return False
    elif medidas[1] > H:
        return False