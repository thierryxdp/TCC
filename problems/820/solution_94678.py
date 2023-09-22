def posLetra(string, letra, n):
    i = 0
    k = 0
    lista = list(string)
    
    while k < n:
        if lista[i] == letra:
            k += 1
        i += 1
    
    return i-1