def repetidos(lista):
    contador = 0
    indice2 = -1
    a = 0
    while contador < len(lista):
        if lista[contador] == lista[indice2]:
            a = a + 1
        else:
            a = a + 0
        contador = contador + 1
        indice2 = indice2 + 1
    return a