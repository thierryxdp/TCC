def repetidos(lista):
    count = 0
    prox = 1
    for i in lista:
        if lista[prox] == lista[prox+1]:
            count = count + i
    prox = prox + 1
    print(count)