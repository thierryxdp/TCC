def colchao(medidas,H,L):
    vol_col=medidas[0]*medidas[1]*medidas[2]
    area_por=H*L
    if vol_col > H*L:
        return False
    elif vol_col < H*L:
        return True