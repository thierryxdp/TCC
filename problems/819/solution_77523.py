def filtraMultiplos(lista,n):
    i=0
    while lista[i]%n==0:
        lista2=lista[i]
        i=i+1
    return lista2