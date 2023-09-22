def repetidos(l):
    old = l[0]
    rep = 0
    
    for i in range(1, len(l)):
        if l[i] == old:
            rep += 1
            
        old = l[i]
    
    return rep