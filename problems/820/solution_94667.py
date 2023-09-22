def posLetra(string, letra, n):
    i = 0
    k = 0
    lista = list(string)
    
    while i < len(lista):
        if lista[i] == letra:
            k += 1
        i += 1
    
    return k