def filtra_pares(notas):
    a=notas[0]
    b=notas[1]
    c=notas[2]
    d=notas[3]
    if a%2!=0:
        a=(,)
    elif b%2!=0:
        b=0
    elif c%2!=0:
        c=0
    elif d%2!=0:
        d=0
    return a+b+c+d