def repetidos(lista):
    repetidor = 0
    contador = 0
    while repetidor < len(lista):
        if lista[repetidor] == lista[repetidor -1]:
            contador = contador + 1
        repetidor = repetidor + 1
    return contador