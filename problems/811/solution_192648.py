def colchao(medida, H, L):
    
    lc = medida[1]
    hc = medida[2]
    if (hc <= H or L) or (lc <= H or L):
        return True
    else:
        return False