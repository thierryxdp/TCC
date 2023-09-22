def filtraMultiplos(lista,n):
    lista = []
    indice = 0
    while lista[indice]%n==0:
        lista += lista[indice]
        indice += 1
    return lista