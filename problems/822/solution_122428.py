def repetidos(lista):
    i=0
    vezes=0
    
    while i<len(lista):
        if lista[i+1]==lista[i]:
            vezes=vezes+1
            i=i+1
            
        else:
            i=i+1
    
    return vezes