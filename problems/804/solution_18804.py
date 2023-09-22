def filtra_pares(n):
    w=n[0]
    x=n[1]
    y=n[2]
    z=n[3]
    par = tuple()
    if w%2==0:
        par+=(w, )
    if x%2==0:
        par+=(x, )
    if y%2==0:
        par+=(y, )
    if z%2==0:
        par+=(z, )
        
        return par