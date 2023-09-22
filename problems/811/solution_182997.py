def colchao(medidas,H,L):
    if medida[1] > H and medida[2] > L:
        return False
    else medida[1] <= H and medida[2] <= L:
        return True