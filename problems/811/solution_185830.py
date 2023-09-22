def colchao(medidas, H, L):
    A, B, C = medidas[0], medidas[1], medidas[2]
    if((B > H and B > L) and (C > H and C > L)):
        return False
    return True