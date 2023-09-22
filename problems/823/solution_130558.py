def faltante(lista):
    i=0
    b=lista[-1]
    a=list(range(b))[1:]
    falta=0
    
    while i<len(a):
        if a[i]!=lista[i]:
            
            falta=falta+a[i]
        else:
        
            i=i+1  
    
    return