def filtra_pares(a,b,c,d):
    pares=()
    num=(a,b,c,d)
    if num[0]%2==0:
        pares+=(a,)
    if num[1]%2==0:
        pares+=(b,)
    if num[2]%2==0:
        pares+=(c,)
    if num[3]%2==0:
        pares+=(d,)
    return pares#Start your python function here