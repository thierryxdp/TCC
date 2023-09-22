def colchao(medidas,H,L):
#Funcao para comparar se o colchao passa pela porta
    if medidas[0] <= H and medidas[1]<= L or medidas[1] <= H and medidas[0]<= L:
        return True
    elif medidas[0] <= H and medidas[2]<= L or medidas[2] <= H and medidas[0]<= L:
        return True
    elif medidas[1] <= H and medidas[2] <= L or medidas[2] <= H and medidas[1] <= L:
        return True
    else:
        return False