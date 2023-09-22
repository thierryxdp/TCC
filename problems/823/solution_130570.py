def faltante(lista):
    i=0
    b=lista[-1]
    a=list(range(b))[1:]
     
    while i<len(a)-1:
        if a[i]!=lista[i]:
            
            num=a[i]
           
        else:
            i=i+1  
    
    return num