def faltante(lista):
    
    i=1
    
    while i<len(lista):
        if i != lista[i-1]:
            return i
        
        i=i+1
    return i