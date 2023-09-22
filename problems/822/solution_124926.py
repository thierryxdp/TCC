def repetidos(lista):
    proximo=0
    acumulador=0
    
    while proximo-1<len(lista):
        proximo1=proximo+1
        if proximo1<len(lista) and lista[proximo1]==lista[proximo]:
            acumulador=acumulador+1
        proximo=proximo+1
    return acumulador