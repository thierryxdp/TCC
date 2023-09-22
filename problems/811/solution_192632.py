def colchao(medidas, H, L):
    [A, B, C] = medidas
    if A or B > H or L:
       return False
    else:
       return True