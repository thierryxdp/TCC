def filtraMultiplos(lista,n):
    i=0
    while lista[i]%n==0:
        lista=[lista[i]]
        i=i+1
    return lista