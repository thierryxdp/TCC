def filtraMultiplos(lista,n):
    divisivel = lista[0:-1]%n==0
    if divisivel in lista:
        return list[divisivel]