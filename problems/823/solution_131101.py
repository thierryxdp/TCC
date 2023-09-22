def faltante(lista):
    contador = 0
    indice = 0
    numerofaltante = 0
    list.append(lista,'0')
    while contador<=len(lista):
        if contador != lista[indice]:
            numerofaltante = contador -1
        else:
            numerofaltante = 0
        contador = contador + 1
        indice = indice + 1
    return contador