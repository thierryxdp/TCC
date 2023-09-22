def filtraMultiplos(lista, n):
    '''recebe uma lista de numeros e um número n, retornando uma lista com os multilpos de n
    lista, int -> lista'''
    i = 0
    listaNova = []
    while i%n != 0:
        i = i+1
    if i%n == 0:
        listaNova = listaNova + [i,]
        i = i + 1
    return listaNova