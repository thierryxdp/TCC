def repetidos(lista):
    cont = 1
    resultado = 0
    while cont < len(lista):
        if lista[cont] == lista[cont -1]:
            resultado += 1
        cont += 1
    return resultado