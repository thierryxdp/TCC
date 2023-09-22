def colchao(medidas,H,L):
    G = []
    G.append(H)
    G.append(L)
    A = medidas[0:2]
    B = medidas[3:6]
    C = medidas[7:10]
    if C < (G[0] or G[1]):
        return True
    elif (C ^ 2) < (H ^ 2 + L ^2) and b < (H or L):
        return True
    else:
        return False