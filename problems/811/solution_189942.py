def colchao(medidas,H,L):
    medidas[0]=0
    vol_col=medidas[0]*medidas[1]*medidas[2]
    area_por=H*L
    if vol_col > area_por:
        return False
    elif area_por > vol_col:
        return True