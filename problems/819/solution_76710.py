def filtraMultiplos(lista,n):
    divisivel= int(lista)%n==0
    if divisivel in lista:
        return divisivel