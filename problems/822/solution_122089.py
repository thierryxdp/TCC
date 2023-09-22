def repetidos(lista):
    proximo=0
    i=0
    while proximo<len(lista):
        if (lista[i]) == (lista[i+1]):
            i=i+1
        proximo=proximo+1
    return i