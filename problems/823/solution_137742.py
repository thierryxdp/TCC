def faltante(num):
    
    i=0
    
    j=1
    
    y=len(num)+2
    
    while i<len(num):
        
        if j in range(1,y):
            i += 1
            j += 1
            
        else:
            return num[i]