def filtra_pares(tupla):
    a=tupla[0]
    b=tupla[1]
    c=tupla[2]
    d=tupla[3]

    if a%2==0:
        return a+b+c+d
    if (b%2==0):
        return a+b+c+d
    if (c%2==0): 
        return a+b+c+d
    if (d%2==0):
        return a+b+c+d
    else:
        return ()