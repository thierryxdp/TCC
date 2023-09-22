def repetidos(lista):
    i=0
    vezes=0
    
    
    
    while i<len(lista):
        while i<len(lista)-1:
            
            if lista[i]==lista[i+1]:
                vezes=vezes+1
                i=i+1
      
            else:
                i=i+1
                vezes=vezes
       
    return vezes