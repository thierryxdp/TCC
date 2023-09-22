def repetidos(lista):
    cont = 0 
    vezes = 0
    while cont < len(lista):
        if lista[cont] == lista[cont-1]:
            vezes += 1
        cont = cont + 1
    return vezes