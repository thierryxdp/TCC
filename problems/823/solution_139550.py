def faltante(lista):
    
    x=len(lista)
    prox=x-1
    
    if x==1 and lista[0]!=1:
        return 1
    elif x==lista[x-1]:
        return lista[x-1]+1
    
    while prox>0:
        if lista[prox]-1!=lista[prox-1] and lista[prox]>lista[prox-1]:
            falta=lista[prox]-1
        
        elif lista[prox]+1!=lista[prox-1] and lista[prox]<lista[prox-1]:
            falta=lista[prox]+1
        
        elif (lista[0]!=1 and lista[prox]>lista[prox-1] ) or (lista[-1]!=1 and lista[prox]<lista[prox-1]):
            falta=1
        
        prox=prox-1
    
    return falta