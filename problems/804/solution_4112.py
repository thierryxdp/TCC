def filtra_pares(t):
    if t[0]%2==0:
        return t[0]
    elif t[0]%2==0 and t[1]%2==0:
        return (t[0],t[1])