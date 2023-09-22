def colchao(medidas,H,L):
    m=max(H,L)
    if medidas[0]<=m and medidas[1]<=m and medidas[2]<=m:
        return True
    if medidas[0]<=m and medidas[1]<=m or medidas[2]<=m:
        return True
    elif max(medidas)<=0:
        return True
    else:
        return False