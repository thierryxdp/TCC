def faltante(lista):
    lista.append(0)
    lista.sort()
    i = 0
    resp = 0
    
    while i < len(lista):
        if(i != lista [i-1] and i != 0):
            resp = i
        i += 1
    return resp