def repetidos(lista):
    contador = 0
    acumulador = []
    list.sort(lista)
    while contador<=len(lista):
        if lista[contador]==lista[contador-1]:
            acumulador = acumulador + (acumulador[contador],)
        contador=contador+1
    return len(acumulador)

#