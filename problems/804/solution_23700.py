def filtra_pares(x):
    f = ()
    
    if x[0]%2==0:
        f = f + tuple(x[0])
    if x[1]%2==0:
        f = f + tuple(x[1])
    if x[2]%2==0:
        f = f + tuple(x[2])
    if x[3]%2==0:
        f = f + tuple(x[3]) 
    return f