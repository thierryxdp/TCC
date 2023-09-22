def repetidos(lista):
    anterior = 0
    proximo = 1
    repetidos = 0
    while proximo < len(lista):
        if lista[anterior] == lista[proximo]:
            repetidos = repetidos + 1
        proximo += 1
        anterior += 1
    return repetidos