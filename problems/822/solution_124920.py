def repetidos(lista):
    proximo=0
    acumulador=0
    
    while proximo<len(lista):
        if lista[proximo+1]==lista[proximo]:
            acumulador=acumulador+1
        proximo=proximo+1
    return acumulador