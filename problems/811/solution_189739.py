def colchao(medidas,H,L):
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if B <= L or C <= H:
        return True
    else:
        return False