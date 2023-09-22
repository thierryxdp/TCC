def colchao(medidas,H,L):
   
    if medidas[1] or medidas[2]>L and H:
        return False
    elif medidas [1] and medidas[2]<L and H:
        return True