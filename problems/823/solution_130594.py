def faltante(lista):
    i=0
    b=lista[-1]
    a=list(range(b))
    c=a[1:]
     
    while i<len(c):
        if a[i]!=lista[i]:
            return a[i]
        else:
            return i+1
    
    return x