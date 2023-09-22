def filtra_pares(x):
    '''Recebe uma tupla, e retorna somente os pares. tupla>int'''
    par = []
    
    if(x[0] % 2 == 0):
        par.append(x[0])
    if(x[1] % 2 == 0):
        par.append(x[1])
    if(x[2] % 2 == 0):
        par.append(x[2])
    if(x[3] % 2 == 0):
        par.append(x[3])
        
    return tuple(par)