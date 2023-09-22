def repetidos(lista):
    i= 0
    rep = 0
    p1=lista[i-1] 
    p2=lista[i]
    while i<=(len(lista)-1):
        p1=lista[i - 1]
        p2=lista[i]
        if p1 == p2:
            rep = rep + 1
        i = i+1
        return rep