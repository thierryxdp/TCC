def faltante(lista):
    contador = 1
    indice = 0
    numerofaltante = 0
    list.append(lista,0)
    while contador<len(lista):
        if contador != lista[indice]:
            numerofaltante = contador
        contador = contador + 1
        indice = indice + 1
    return numerofaltante