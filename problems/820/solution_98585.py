def posLetra(string,letra,posicao):
    ''''''
    acumulador = []
    contador = 0
    while contador < len(string):
        if string[contador] == letra:
            list.append(acumulador, contador)
        contador = contador + 1
    return acumulador[posicao]