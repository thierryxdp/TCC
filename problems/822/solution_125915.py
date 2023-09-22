def repetidos (lista):
    proximo=0
    repetidas=0
    while proximo < len (lista):
        if lista[proximo]==lista[proximo+1]:
            repetidas=repetidas+1
        proximo=proximo+1
    return repetidas