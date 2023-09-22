def melhor_volta(matriz):
    
    n_linha=len(matriz)
    n_coluna=len(matriz[0])
     R=[]
        
    for i in range(n_linha):
        linha = linha + n_coluna *[0]
        
    for i in range(n_linha):
        for j in (n_coluna):
            R[i][j]=matriz[i][j]
            
    return min(R)