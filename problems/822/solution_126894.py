def repetidos(lista):
    i=1
    resultado=0
    while i<len(lista):
        if lista[i]==lista[i-1]:
            resultado += 1
        i += 1
    return resultado