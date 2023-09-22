def colchao(medidas,H,L):
    if medidas[1]<=L or medidas[2]<=L or medidas[1]<=H or medidas[2]<=H:
        return True
    else:
        return False