def media_matriz(mtx):
    n_lin     = len(mtx)
    n_col     = len(mtx[0])
    contador  = 0
    soma      = 0
    
    for i in range(n_lin):
        for j in range(n_col):
            soma     = soma + mtx[i][j]
            contador = contador + 1
    
    return round(soma/contador,2)