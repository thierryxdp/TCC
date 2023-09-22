def filtra_pares(a,b,c,d):
    pares=()
    num=(a,b,c,d)
    if num[0]%2==0:
        pares+=(a,)
    elif num[1]%2==0:
        pares+=(b,)
    elif num[2]%2==0:
        pares+=(c,)
    elif num[3]%2==0:
        pares+=(d,)
    return pares