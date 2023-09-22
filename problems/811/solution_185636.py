def colchao(medidas,H,L):
    a,b,c=medidas
    if a<L and (b<H or c<H):
        return True
    else:
        return False