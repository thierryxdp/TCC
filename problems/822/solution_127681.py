def repetidos(li):
    
    i= 0
    rep = 0
    pos1 = li[i- 1] 
    pos2 = li[i]
    
    while i <= (len(li)- 1):
        pos1 =li[i- 1]
        pos2 = li[i]
        if pos1== pos2:
            rep= rep+ 1
        i+= 1
        
        
    return rep