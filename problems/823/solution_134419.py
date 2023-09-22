def faltante(lista):
    i=0
    n=1
    faltante=''
    while i<len(lista)+1:
        if n in lista:
            n=n+1            
        elif n not in lista:
            faltante=n
    	i=i+1
    return faltante