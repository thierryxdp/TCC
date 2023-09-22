def posLetra(string,letra,n):
    tam=len(string)
    cont=0
    cont2=0
    
    while cont<tam:
        if string[cont]==letra:
        	cont2=cont2+1
            
        if cont2==n:
            break
        
        if cont2<n:
            return -1
        
        cont=cont+1
        
    return cont