def filtra_pares(num):
    par = ()
    if num[0] %2==0:
        return par = par + (num[0],)
    if num[1] %2==0:
        return par = par + (num[1],)
    if num[2] %2==0:
        return par = par + (num[2],)
    if num[3] %2==0:
        return par = par + (num[3],)
    else:
        return par = par