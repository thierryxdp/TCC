def faltante(num):
    
    i=0
    
    while i<len(num):
        
        if num[i] not in range(1,num+1):
            return num[i]
            
        i += 1