def faltante(lista):
    
    list.sort(lista)
    faltantes = 0
    i = 0
    
    while i < len(lista):
        if lista[i] - i == 2:
            faltantes += 1
        i += 1
    if faltantes == 0:
        return lista[-1] + 1
    else:
        return lista[-1] - faltantes