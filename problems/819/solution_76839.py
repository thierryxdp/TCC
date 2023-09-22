def filtraMultiplos(lista,n):
    listaNew = 0
    i = 0
    listaMultiplos = []
    while i < len(lista):
        if lista[i] % n == 0:
        	listaNew = listaNew + lista[i]
        	listaMultiplos = [listaNew]
       	i = i + 1
    return listaMultiplos