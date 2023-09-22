def faltante(lista):
    contador = 1
    indice = 0
    acumulador = 0
    while contador<=len(lista)+1:
        if contador != lista[indice]:
            acumulador = acumulador + contador 
        contador = contador + 1
        indice = indice + 1
    return acumulador