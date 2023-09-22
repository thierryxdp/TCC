def repetidos(lista):
    contador = 0
    acumulador = 0
    
    
    while contador<len(lista)-1:
        if lista[contador+1]==lista[contador]:
            acumulador=acumulador+1
        contador=contador+1
            
           
    return acumulador