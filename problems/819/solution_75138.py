def filtraMultiplos(lista,numero):
    l=lista
    n=numero
    x=0
    while l[x]<=n:
        if l[x]%n==0:
            return l[x]
        x=x+1
    return l[x]