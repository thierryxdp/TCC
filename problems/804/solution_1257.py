def filtra_pares(lista):
    lista = (lista[0],lista[1],lista[2],lista[3],lista[4])
    lista1 = filter(lambda x: x % 2 == 0,lista) 
    return list(lista1)