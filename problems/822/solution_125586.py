def repetidos (lista):
    
    rep = 0
    i = 0
    lista.sort()
    
    while i < len((lista)-1):
        if lista[i] == (lista[i+1]): 
            rep = rep + 1
        i = i + 1
    return rep