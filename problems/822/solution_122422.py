def repetidos(lista):
    i=0
    lista2=[]
    
    while i<len(lista):
        
        if lista[i]==lista[i-1]:
            lista2=lista+[i]
            
        i=i+1
        
    return len(lista2)