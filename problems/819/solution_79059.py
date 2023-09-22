def filtraMultiplos(lista, n):
    
    numeros = lista
    divisor = n
    
    return list(filter(lambda x: x % divisor == 0, numeros))