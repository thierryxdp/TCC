def repetidos(lista):
    repetido=0
    i=0
    while i<len(lista):
        if lista[i+1]==lista[i]:
            repetidos=repetidos+1
        i=i+1
        return repetidos