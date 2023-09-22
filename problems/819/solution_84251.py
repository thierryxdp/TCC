def filtraMultiplos(ln, n):
    
    lista = []

    for x in ln:
        if x%n == 0:
            lista.append(x)
    return lista