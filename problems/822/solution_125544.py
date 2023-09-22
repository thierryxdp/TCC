def repetidos (lista):
    
    rep = 0
    i = 0
    while i < len(lista):
        if lista.count(lista[i])>1: 
            rep = rep + 1
        i = i + 1
    return rep