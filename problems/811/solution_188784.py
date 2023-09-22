def colchao(medidas,H,L):
    if medidas[2] <= H and medidas[1] <=L:
        return True
    elif medidas[1] <= L:
        return True
    elif medidas[0]<=L and medidas[1]<= H:
        return True
    else: 
        return False