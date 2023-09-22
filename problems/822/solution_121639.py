def repetidos(numeros):

    indice = 1
    listadeindices = []

    while indice < len(numeros):
        if numeros[indice] == numeros[indice-
            listadeindices += [numeros[indice]]
        indice += 1

    return len(listadeindices)