def faltante(lista):
    i=0
    n=len(lista)
    a=lis(range(len(n-1)))[1:]
    
    while i<len(a):
        if a[i]!=lista[i]:
            falta=a[i]
        
        i=i+1
    return falta