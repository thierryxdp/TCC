def colchao(medidas,H,L):
    m = min(medidas)
    medidas.remove(max(medidas))
    M2 = max(medidas)
    
    if H >= M2 and L >= m or H >= m and L >= M2:
        return True
    else:
        return False