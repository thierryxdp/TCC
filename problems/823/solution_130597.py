def faltante(lista):
    i=0
    b=lista[-1]
    a=list(range(b))
    c=a[1:]
     
    while i<len(c):
        if c[i]==lista[i]:
            return i+1
        else:
            return c[i]
    
    return c[i]