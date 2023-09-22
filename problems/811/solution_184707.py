def colchao(medidas,H,L):
    m = min(medidas)
    medidas.remove(max(medidas))
    M2 = max(medidas)
    
    if H >= M2 and L >= m:
        return True
    else:
        return False