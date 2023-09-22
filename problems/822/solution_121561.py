def repetidos(lista):

    contador = 0
    acumuladora = 0
    lista.sort()

    while contador < len(lista)-1:
        if lista[contador] == lista[contador]:
            acumuladora += 1
        contador += 1

    return acumuladora