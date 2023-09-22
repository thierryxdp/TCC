def filtraMultiplos(lista,numero):
    multiplos=()
    x=0
    while lista[x]>=n:
        if lista[x]%n==0:
            multiplos=multiplos+(lista[x],)
        x=x+1
    return multiplos