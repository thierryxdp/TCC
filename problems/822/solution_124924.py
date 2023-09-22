def repetidos(lista):
    proximo=0
    acumulador=0
    
    while proximo-1<len(lista):
        if lista[proximo]==lista[proximo]:
            acumulador=acumulador+1
        proximo=proximo+1
    return acumulador