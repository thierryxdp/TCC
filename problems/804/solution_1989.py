def filtra_pares(t):
    s=()
    for i in t:
        if i%2==0:
            s=s+(i,)
    return s