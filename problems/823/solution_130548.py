def faltante(lista):
    i=0
    n=len(lista)
    a=list(range(n))[1:]
    
    while i<len(a)-1:
        if a[i]!=lista[i]:
            falta=a[i]
        
        i=i+1
    return falta