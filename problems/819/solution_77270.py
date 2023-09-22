def filtraMultiplos(lista,n):
    lista_multiplos=[termo for termo in lista if termo %n==0]
    multiplos=lista_multiplos
    return multiplos