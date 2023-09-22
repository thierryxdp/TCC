def repetidos(lista):
    
    
    i=0
    contador=0
    
    while(i<len(lista)):
        if lista[i]==lista[i+1]:
            contador=contador+1
        else:
            contador=contador
        i=i+1
        
        
        return contador