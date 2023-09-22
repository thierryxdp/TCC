def repetidos(lista):
    acc = 0
    for x in range(len(lista)):
        if lista[x] == lista[x-1]:
            acc +=1
    return acc