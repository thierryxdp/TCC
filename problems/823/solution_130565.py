def faltante(lista):
    i=0
    b=lista[-1]
    a=list(range(b))[1:]
    
    
    while i<len(a):
        if a[i]!=lista[i]:
            
            falta=lista[i]
            i=i+1
        else:
            i=i+1  
    
    return falta