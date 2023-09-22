def colchao(medidas,H,L):
    c = medidas[0]
    l = medidas[1]
    h = medidas[2]
    
    if l > H and h > L:
        return False
    elif l <= H and h <= L:
        return True