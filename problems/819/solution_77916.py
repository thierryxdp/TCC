def filtraMultiplos(lista,n):
    
    i=0 
    multiplos=" "
    
    while(i<len(lista)):
        if lista[i]%n == 0:
            list.append(multiplos,lista[i])
            
        i=i+1 
        
        return multiplos