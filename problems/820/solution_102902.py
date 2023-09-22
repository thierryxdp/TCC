def posLetra(texto,letra,num):
    """
    str,str,int->"""
    
    i = 0
    j = 0
    
    while i < len(texto):
        
        if texto[i] == letra:
            j += 1
            if j == num:
                return i
        i+=1
            
    return -1