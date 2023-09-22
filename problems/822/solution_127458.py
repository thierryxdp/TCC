def repetidos(lista):
    i=0
    a=0
    
    while i+1< len(lista)-1:
        if lista[i-1]==lista[i] and lista[i-1]!= lista[i+1]:
            
            	a+=1 
        i+=1
        if lista[i-1]==lista[i] and i== len(lista)-1:
        	a+=1    
    return a