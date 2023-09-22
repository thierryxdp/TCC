def colchao(medidas,H,L):
    m=max(H,L)
    if medidas[0]<=m and medidas[1]<=m and medidas[2]<=m:
        return True
    else:
        return False