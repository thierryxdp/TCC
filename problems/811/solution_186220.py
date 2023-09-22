def colchao(medidas,h,l):
    if (medidas[1] > l and h) and (medidas[2] > l and h):
        return False
    
    if (medidas[1] < l or h) and (medidas[2] < l or h):
        return True