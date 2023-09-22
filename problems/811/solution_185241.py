def colchao(medidas,H,L):
    a,b,c=medidas
    if a<L and (b<H or c<L):
        return True
    else:
        return False