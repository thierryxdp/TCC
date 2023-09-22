def faltante(lista):
    i=0
    a=list(range(len(lista)))[1:]
    
    
    while i<len(a):
        if a[i]!=lista[i]:
            falta=a[i]
        
        i=i+1
    return falta