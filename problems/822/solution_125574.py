def repetidos (lista):
    
    rep = 0
    i = 0
    lista.sort()
    
    while i < len(lista):
        if lista[i]==lista[i+1]: 
            rep = rep + lista.count(lista[i])
        i = i + 1
    return rep