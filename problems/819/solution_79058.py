def filtraMultiplos(lista, n):
    
    numeros = lista
    divisor = n
    
    return list(filter(lambda x, n: x % divisor == 0, numeros))