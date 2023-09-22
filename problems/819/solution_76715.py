def filtraMultiplos(lista,n):
    lista = lista[0:-1]
    divisivel = lista%n==0
    if divisivel in lista:
        return list[divisivel]