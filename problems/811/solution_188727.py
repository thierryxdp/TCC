def colchao(medidas,H,L):
    A = int(medidas[0])
    B = int(medidas[1])
    C = int(medidas[2])
    if (B > H and L): return False
    if (C > H and L): return False
    if (L > B > H): return True
    if (L < B < H): return True
    if (L < B > H): return True 
    if (L > C > H): return True
    if (L < C > H): return True
    if (L > C > H): return True