colchao(medidas, H ,L ):
    if medidas[0] > L:
        return False
    if medidas[1] > L:
        return False
    if medidas[2] > L:
        return False
    if medidas[0] < L:
        return False
    if medidas[1] < L:
        return False
    if medidas[2] < L:
        return False
    else:
        return True