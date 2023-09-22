def filtra_pares(num):
    pares = ()
    if num[0] %2==0:
        pares = pares + (num[0],)
    if num[1] %2==0:
        pares =  pares + (num[1],)
    if num[2] %2==0:
        pares = pares + (num[2],)
    if num[3] %2==0:
        pares = pares + (num[3],)
    else:
        pares = pares