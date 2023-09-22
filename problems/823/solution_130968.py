def faltante(lista):
    i=0
    lista.sort()
    
    while i<len(lista):
        
        if lista[i] != i:
            return i+1
        i = i + 1  
        return i+1