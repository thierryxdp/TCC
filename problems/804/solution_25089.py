def filtra_pares(a):
    b=()
    c=list(a)
    if c[0]%2==0:
        b.append(c[0])
    if c[1]%2==0:
        b.append(c[1])
    if c[2]%2==0:
        b.append(c[2])
    if c[3]%2==0:
        b.append(c[3])
    return b