def colchao(medidas,H,L):
    medidas=[A,B,C]
    if (A<=H and A<=L) and (B<=H or B<=L):
        return True
    else:
        return False