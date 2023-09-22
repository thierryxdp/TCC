def repetidos (lista):
    
    rep = 0
    i = 0
    while i < len(lista):
        rep=lista.count(lista[i]) + 1
        i = i + 1
    return rep