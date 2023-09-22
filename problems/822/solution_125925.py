def repetidos (lista):
    proximo=0
    repetidas=0
    while (proximo+1) <= len (lista):
        if lista[proximo-1]==lista[proximo]:
            repetidas=repetidas+1
        proximo=proximo+1
    return repetidas