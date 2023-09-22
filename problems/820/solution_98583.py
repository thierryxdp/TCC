def posLetra(string,letra,posicao):
    ''''''
    acumulador = []
    contador = 0
    while contador < len(string):
        if string[contador] == letra:
            lista.append(acumulador, contador)
    return acumulador[posicao]