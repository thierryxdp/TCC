def repetidos(lista):
    proximo=0
    acumulador=0
    
    while proximo<len(lista):
        proximo1=proximo +1
        if lista[proximo1]==lista[proximo]:
            acumulador=acumulador+1
        proximo=proximo+1
    return acumulador