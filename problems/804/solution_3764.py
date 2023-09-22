def filtra_pares(x,y,z,w):
    """filtra os elementos da tupla, retornando apenas os pares na mesma ordem"""
    if (x % 2 = 0) and (y % 2 = 0) and (z % 2 = 0) and (w % 2 = 0):
        return x,y,z,w
    elif (x % 2 = 0) and (y % 2 = 0) and (z % 2 = 0):
        return x,y,z
    elif (x % 2 = 0) and (y % 2 = 0):
        return x,y
    elif x % 2 = 0:
        return x
    elif y % 2 = 0:
        return y
    elif z % 2 = 0:
        return z
    elif w % 2 = 0:
        return w
    elif (y % 2 = 0) and (z % 2 = 0):
        return y,z