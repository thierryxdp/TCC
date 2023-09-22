def colchao(medidas,H,L):
    
    medidas[1]=B
    medidas[2]=C
    if B or C > H:
        return False
    elif B or C < H:
        return True
    else:
        if B or C < L:
            return True