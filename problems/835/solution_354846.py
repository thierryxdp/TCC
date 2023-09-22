def melhor_volta(matriz):
    """list(list) -> int,float,int"""
    """retorna quem fez a melhor volta dos corredores"""
    
    V = matriz[0][0]
    M = []
    
    for m in matriz:
        if min(m) < V:
            V = min(m)
            M = m
            pass
        pass
    
    C = list.index(matriz,M)
    P = list.index(M,V)
    
    return (C,V,P)