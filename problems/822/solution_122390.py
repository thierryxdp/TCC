def repetidos(lista):
    i=0
    repetidos=0
    while (i<len(lista)):
        if (lista[i+1]==lista[i]):
            repetidos=repetidos+1
        i=i+1
        return repetidos