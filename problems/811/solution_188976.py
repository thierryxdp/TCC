def colchao(medidas,H,L):
    A = medidas[0]
    B = medidas[1]
    C = medidas [2]
    if medidas[0]<L and medidas[1]<=H or medidas[1]<L:
        return True
  	else:
        return False