def inverte(l):
    
    k=".?!;:,-"
    
    g=[]
    
    for x in l:
        if x in k:
            g.append(x)
            
    return g