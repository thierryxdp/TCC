def colchoes(medidas,H,L):
    medidas[0]=A
    medidas[1]=B
    medidas[2]=C
    if (B<=L and C<=H)or(C<=L and B<=H)or(B<=L and A<=H)or(A<=L and C<=H)or(C<=L and A<=H)or(A<=H and B<=H):
        return True
    else:
        return False