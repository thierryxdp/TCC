def colchao(medidas,h,l):
    
    
    if (medidas[1] < l or h) and (medidas[2] < l or h):
        return True
    
    if (medidas[1] > l and h) or (medidas[2] > l and h):
        return False