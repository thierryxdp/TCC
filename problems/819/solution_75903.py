def filtraMultiplos(lista,n):
    """ """ 
    n=0
    i=0
    while n<len(lista):
        if i%n == 0:
            return i
        lista=lista[i]
    return lista