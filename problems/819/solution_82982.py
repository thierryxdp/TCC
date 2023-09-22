def filtraMultiplos(lista,n):
    lista_multiplos = []
    indice = 0
    while lista[indice]%n==0:
        lista_multiplos += lista[indice]
        indice += 1
    return lista