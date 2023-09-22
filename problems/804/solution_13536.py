def filtra_pares(t):
    pares=()
    if t[0]%2==0:
        pares=t[0],
    if t[1]%2==0:
        pares1=t[1],
        pares= pares+pares1
    if t[2]%2==0:
        pares2=t[2],
        pares=pares+pares2
    if t[3]%2==0:
        pares3=t[3],
        pares= pares+pares3
        return pares
    
    #Start your python function here