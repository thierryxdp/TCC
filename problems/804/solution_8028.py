def filtra_pares(x):
    n=()
    if x[0]% 2==0:
        n=n+(x[0],)
    if x[1]% 2==0:
        n=n+(x[1],)
    if x[2]% 2==0:
        n=n+(x[2],)
    if x[3]% 2==0:
        n=n+(x[3],)
        
    return n