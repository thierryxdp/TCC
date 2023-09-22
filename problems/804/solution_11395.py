def filtra_pares (x):
    x = (filtra_pares[0],filtra_pares[1],filtra_pares[2],filtra_pares[3])
    a = filtra_pares[0]%2
    b = filtra_pares[1]%2
    c = filtra_pares[2]%2
    d = filtra_pares[3]%2
    if a==0:
        return filtra_pares[0]
    if b==0:
        return filtra_pares[1]
    if c==0:
        return filtra_pares[2]
    if d==0:
        return filtra_pares[3]