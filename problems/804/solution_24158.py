def filtra_pares(t):
    """ recebe uma tupla de 4 elementos int e retorna uma
    	nova tupla com apenas os números pares
        int -> int"""
    lista = []
    for i in t:
        if i%2==0:
            lista.append(i)
    return tuple(lista)