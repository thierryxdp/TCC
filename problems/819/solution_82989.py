def filtraMultiplos(lista,n):

    i=0
    
    novalista=[]
    
    while i<len(lista):
        if lista[i]%n==0:
            x=lista[i]
            novalista.append(x)
            i += 1
        
        else:
            i += 1
    
    return novalista