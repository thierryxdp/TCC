def media_matriz(matriz):
    """list(list) -> float"""
    """retorna a média de todos os termos da matriz"""
    
    M = 0
    
    for m in matriz:
        M += sum(m)/len(m)
        pass
    
    M = M/len(matriz)
    
    return round(M,2)