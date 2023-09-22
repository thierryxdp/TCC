def repetidos(lista):
    cont = 0
    repet = 0
    while (cont < len(lista)):
        if rept < lista.count(lista[cont]):
            rept = lista.count(lista[cont])
        cont = cont + 1
    return repet