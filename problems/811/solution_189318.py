def colchao(medidas,H,L):
    m=max(H,L)
    n=min(H,L)
    if int(medidas[2])<=m and int(medidas[1]<=n):
        return True
    else:
        return False