def posLetra(string,letra,n):
    tamanho=len(string)
    cont1=0
    cont2=0
    
    while cont1<tamanho:
        if string[cont1]==letra:
        	cont2=cont2+1
            
        if cont2==n:
            break
        
        cont1=cont1+1
        
    if cont2<n:
        return -1
    return cont1