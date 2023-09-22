def faltante(lista):
    
    n=len(lista)
    p=n-1
    
    if n==1 and lista[0]!=1:
        return 1
    elif n==lista[n-1]:
        return lista[n-1]+1
    
    while p>0:
        if lista[p]-1!=lista[p-1] and lista[p]>lista[p-1]:
            falta=lista[p]-1
        
        elif lista[p]+1!=lista[p-1] and lista[p]<lista[p-1]:
            falta=lista[p]+1
        
        elif (lista[0]!=1 and lista[p]>lista[p-1] ) or (lista[-1]!=1 and lista[p]<lista[p-1]):
            falta=1
        
        p-=1
    
    return falta