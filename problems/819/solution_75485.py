def filtraMultiplos(lista, n):
    multiplos=[]
    proximo=0
    while proximo<len(lista):
        if lista[proximo]%n==0:
            multiplos=proximo+1
            return multiplos