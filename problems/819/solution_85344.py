def filtraMultiplos(lista,n):
    c=0
    d=[]
    a=len(lista) - 1
    while c<len(lista):
        if lista[c]%n == 0:
            d=d + lista[c]
        c=c+1
    return d