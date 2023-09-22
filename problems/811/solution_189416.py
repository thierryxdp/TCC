def colchao(medidas,H,L):
    a1=medidas[1]*medidas[2]+medidas[0]*medidas[2]
    a2=H*L
    if a1<a2:
        return True
    else:
        return False