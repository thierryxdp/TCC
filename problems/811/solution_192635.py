def colchao(medidas, H, L):
    [A, B, C] = medidas
    if A > H or L:
       return False
    elif B > H or L:
       return False
    else:
       return True