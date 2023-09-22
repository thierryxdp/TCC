def filtra_pares(t):
    vazio=()
    for x in t:
        if x%2==0:
            vazio+=(x,)
            
    return vazio