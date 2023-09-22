def filtraMultiplos(lista, n):
    
    numeros = lista
    
    return list(filter(lambda x, n: x % n == 0, lista))