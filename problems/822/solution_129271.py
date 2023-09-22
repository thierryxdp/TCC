def repetidos(lista):
    count = 0
    prox = 1
    for i in lista:
        if lista[0] == lista[prox]:
            count = count + lista[0]
    prox = prox + 1
    return(count)