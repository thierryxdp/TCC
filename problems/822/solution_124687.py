def repetidos(lista):
    cont = 0
    repet = 0
    while (cont < len(lista)):
        if repet < lista.count(lista[cont]):
            repet = lista.count(lista[cont])
        cont = cont + 1
    return repet