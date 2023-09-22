def inverte(l):
    
    k=".?!;:,-"
    
    g=[]
    
    for x in l:
        if x not in k:
            g.append(x)
    
    k=list.join(g)
            
    return k