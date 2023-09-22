def faltante(num):
    
    i=0
    
    y=len(num)+2
    
    while i<len(num):
        
        if num[i] not in range(1,y):
            i += 1
            
        else:
            return num[i]