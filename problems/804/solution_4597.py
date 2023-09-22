#Start your python function here
def filtra_pares(a,b,c,d):   
    pares = 0
    if a %2 ==0:
        pares = pares.append(a)
    elif b %2 ==0:
        pares = pares.append(b)
    elif c %2 ==0:
        pares = pares.append(c)
    elif d %2 ==0:
        pares = pares.append(d)
    return (pares)