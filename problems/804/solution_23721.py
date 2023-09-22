def filtra_pares(x):
    x = (a,b,c,d)
    f = []
    if x[0]%2==0:
        f.append(x[0])
    if x[1]%2==0:
        f.append(x[1])
    if x[2]%2==0:
        f.append(f[2])
    if x[3]%2==0:
        f.append(f[3])
        tuple(f)