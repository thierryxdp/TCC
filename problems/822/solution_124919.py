def repetidos(lista):
    proximo=0
    contador=0
    acumulador=0
    
    while proximo<len(lista):
        if lista[contador+1]==lista[contador]:
            acumulador=acumulador+1
        proximo=proximo+1
        contador=proximo+1
    return acumulador