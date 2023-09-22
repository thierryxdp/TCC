def repetidos(lista):
    i=0
    vezes=0
    a=i
    
    
    while i<len(lista):
        while i<=len(lista)-1:
            
            if lista[i]==lista[a]:
                vezes=vezes+1
                i=i+1
            
            else:
                i=i+1
                vezes=vezes-1
    
    return vezes