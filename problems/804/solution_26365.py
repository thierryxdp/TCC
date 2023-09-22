def filtra_pares(a,b,c,d):
    inteiros=(a,b,c,d)
    pares=()
    if inteiros[0]%2==0:
        pares=pares+a
    if inteiros[1]%2==0:
        pares=pares+b
    if inteiros[2]%2==0:
        pares=pares+c
    if inteiros[3]%2==0:
        pares=pares+d
    return pares
#Start your python function here