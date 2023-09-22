def repetidos(lista):
    cont = 1
    while cont < len(lista):
        resultado = 0
        if lista[cont] == lista[cont - 1]:
            resultado += 1
        cont += 1
    return resultado