def colchao(medidas,H,L):
    A = medidas[0:2]
    B = medidas[3:6]
    C = medidas[7:10]
    if C < (H or L):
        return True
    elif (C ^ 2) < (H ^ 2 + L ^2) and b < (H or L):
        return True
    else:
        return False