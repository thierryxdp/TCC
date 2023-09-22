def colchao(medidas,H,L):
    A = int(medidas[0])
    B = int(medidas[1])
    C = int(medidas[2])
    if (B + C > H + L): return False
    if (B > H and L): return False
    if (C > H and L): return False
    else: return True