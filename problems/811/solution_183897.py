def colchao(medidas,H,L):
    area_porta = H*L
    if medidas[1] > H and medidas[2] > H:
        return False
    else:
        return True