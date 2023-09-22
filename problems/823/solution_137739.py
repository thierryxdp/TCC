def faltante(num):
    
    i=0
    
    while i<len(num):
        
        if num[i] not in range(1,len(num)+1):
            i += 1
            
        else:
            return num[i]