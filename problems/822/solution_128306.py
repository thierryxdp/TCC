def repetidos(lista):
    acc = 0
    while 0<x<len(lista):
        if lista[x] == lista[x-1]:
            acc +=1
    return acc