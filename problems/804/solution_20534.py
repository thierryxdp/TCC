def filtra_pares(x):
    pares_2=()
    if x[0]%2==0:
        pares_2=pares_2+(x[0],)
    if x[1]%2==0: 
        pares_2=pares_2+(x[1],)
    if x[2]%2==0: 
        pares_2=pares_2+(x[2],)
    if x[3]%2==0:  
        pares_2=pares_2+(x[3],)
    return pares_2