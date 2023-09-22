def faltante(num):
    
    i=0
    
    while i<len(num):
        
        for num[i] not in range(1,len(num)+1):
            return num[i]
            
        i += 1