def filtraMultiplos(lista,n):
    multiplos=0
    p=0
    while p<len(lista):
        if lista[p]%n == 0:
            multiplos = multiplos + lista[p]
        p=p+1    
    return multiplos