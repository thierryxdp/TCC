def colchao(medidas, H, L):
    [A, B, C] = medidas
    if A > H or L:
       return False
    if B > H or L:
       return False
    else:
       return True