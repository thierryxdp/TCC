colchao(medidas,H,L):
    
    a = medidas[0]
    b = medidas[1]
    
    if (a <= H and b <= L) or (b <= H and a <= L):
        return True
    else:
        return False