def repetidos(lista):
    i=0
    repetidos=0
    proximo=0
    while proximo<len(lista):
        if (lista[i+1])==(lista[i]):
            repetidos=repetidos+1
        proximo=proximo+1
        i=i+1
    	return repetidos