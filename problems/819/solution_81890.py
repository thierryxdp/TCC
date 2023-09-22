def filtraMultiplos(numeros, n):
    lista = []
    for c in numeros: 
        if c%n == 0: 
            lista.append(c)
    return lista