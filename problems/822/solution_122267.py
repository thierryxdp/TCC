def repetidos(lista):
    i=0
    lista1=list.sort(lista)
    repetidos=0
    while i<len(lista):
        if lista1[i+1]==lista1[i]:
            repetidos=repetidos+1
        i=i+1
        return repetidos