def filtra_pares(x):
    num=len(x)
    par=[]
    for i in range (num):
        
        if x[i] % 2 == 0:
            
            par.append(x[i])
            
    return tuple(par)