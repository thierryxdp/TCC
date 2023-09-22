def colchao(medidas,H,L):
    import math
    b = medidas[1]
    diag = math.sqrt((H**2)+(L**2))
    if (L>=b):
        return True
    elif (diag>=b):
        return True
    else:
        return False