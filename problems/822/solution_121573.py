def repetidos(lista):

    contador = 0
    acumuladora = 0
    

    while contador < len(lista)-1:
        if lista[contador+1] == lista[contador]:
            acumuladora += 1
        contador += 1

    return acumuladora