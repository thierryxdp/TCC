def colchao(medida, H, L):
    
    lc = medida[1]
    hc = medida[2]

    if H >= hc or L >= hc:
        return True
    if H >= lc or L >= lc:
        return True
    else:
        return False