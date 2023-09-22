def filtraMultiplos(lista,n):
    proximo=1
    multiplos=[]
    while proximo<len(lista):
        if lista[proximo]%n==2:
            multiplos=multiplos+(lista[proximo],)
        proximo=proximo+1
    return multiplos