def busca(area,mtx):
    
    n_lin = len(mtx)
    n_col = 4
    A = []
    P = []
    L = []
    
    for i in range(n_lin):
        A.append( [0] * 3) 
        
    
    for i in range(n_lin):
        for j in range(4):
            if (j != 2):
                
                if (j == 0 or j == 1):
                    K          = mtx[i][j]
                    A[i][j]    = K
                
                if (j == 3):
                    K          = mtx[i][j]
                    A[i][j-1]    = K
    
    for i in range(n_lin):
        for j in range(n_col):
            if (mtx[i][j] == area):
                P.append(i)
                
    
    for i in P:
        L.append(A[i])
        
    
    return L