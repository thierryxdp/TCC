def filtraMultiplos(lista,numero):
    l=lista
    n=numero
    x=0
    while l[x]%n==0:
        lista1=[l[x]]
    x=x+1
    return x