def colchao(medidas,H,L):
    if H > medidas[1] or medidas[2] or L > medidas[1] or medidas[2]:
        return True
    if H < medidas[1] or medidas[2]:
        return False
    if L < medidas[1] or medidas[2]:
        return False