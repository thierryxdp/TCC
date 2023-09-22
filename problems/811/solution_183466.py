def colchao(medidas,H,L):
    A,B,C = medidas[0],medidas[1],medidas[2]
    if B <= H and A <= 100:
        return True
    else:
       return False