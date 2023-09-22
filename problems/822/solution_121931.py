def repetidos(lista):
    vezes=0
    i=0
    contador=0
    while i < len(lista):
        if lista[i] in lista[i+1:] and lista[i] in lista[i+2:]:
            vezes=vezes + 1
            
          
        
        elif lista[i] in lista[i+1:] :
            contador= contador + 1
            
    
            
        i=i+1
        
    return vezes