def faltante(lista):
    i=0
    b=lista[-1]
    a=list(range(b))
     
    while i<len(a):
        if a[i]!=lista[i]:
            num=a[i]
        
            i=i+1
    
    return num