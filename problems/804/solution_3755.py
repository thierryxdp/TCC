def filtra_pares(b):
    a=[]
    if b[0]%2==0:
        a.append(b[0])
    if b[1]%2==0:
        a.append(b[1])
    if b[2]%2==0:
        a.append(b[2])
    if b[3]%2==0:
        a.append(b[3])
    a=tuple(a)
    return (a)