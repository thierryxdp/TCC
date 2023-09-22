def colchao(medidas, h, l):
    if medidas[1] <= h:
        return True
    elif medidas[2] <= h:
        return True
    elif medidas[1] > h and medidas[2] <= h:
        return True
    elif medidas[2] > h and medidas[1] <= h:
        return True
    elif medidas[1] > h and medidas[2] <= l:
        return True
    elif medidas[2] > h and medidas[1] <= l:
        return False
    else:
        return False