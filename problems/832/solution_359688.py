def eh_quadrada(matriz):
    
    
    n_linha=len(matriz)
    n_coluna=len(matriz[0])
        
        
    for i in range(n_linha):
        for j in range(n_coluna):
            if matriz == 0:
                return False