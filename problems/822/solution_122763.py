def repetidos(lista):
    count = 0
    prox = 1
    while prox < len(lista):
        if lista[prox] == lista[prox+1]:
            count = count + 1
    prox = prox +1
    return count