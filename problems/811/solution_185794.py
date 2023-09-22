def colchao(medidas,H,L):
    A,B,C = medidas
    medidas = A*B*C
    if 0<medidas<=25 and 0<H<=200 and 0<L<=220:
        return True
    else:
        return False