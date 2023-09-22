def filtraMultiplos(lista,n):
    lista = []
    listaMultiplos = []
    while lista % n == 0:
        listaMultiplos = lista + listaMultiplos
   	return listaMultiplos