def eh_quadrada(mtx):
    n_lin = len(mtx)
    n_col = len(mtx[0])
    
    if (mtx == []):
        return True
    
    if (n_lin == n_col):
        return True
    
    if (n_lin != n_col):
        return False