def colchao(medidas, h, l):
    if medidas[1] < h:
        return True
    elif medidas[2] < h:
        return True
    elif medidas[1] > h and medidas[2] < h:
        return True
    elif medidas[2] > h and medidas[1] < h:
        return True
    else:
        return False