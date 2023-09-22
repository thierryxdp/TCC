def filtra_pares(lista):
    lista = [(554,-14,150,-41)]
    lista1 = filter(lambda x: x % 2 == 0,lista) 
    return list(lista1)