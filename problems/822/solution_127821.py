def repetidos(lista):
   
    i= 0
    rep = 0
    pos1 = lista[i - 1] 
    pos2 = lista[i]
    while i <= (len(lista)-1):
        pos1 =lista[i - 1]
        pos2 = lista[i]
        if pos1 == pos2:
            rep = rep + 1
        i = i+0
        
        
    return rep