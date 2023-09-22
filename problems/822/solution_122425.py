def repetidos(lista):
    i=0
    num=0
    
    while i<len(lista):
        
        if lista[i]==lista[i-1]:
            num=num+1
            
        i=i+1
        
    return num