def posLetra(string,letra,posicao):
    ''''''
    acumulador = []
    contador = 0
    while contador < len(string):
        elif str.count(string) < posicao:
            return -1
        if string[contador] == letra:
            list.append(acumulador, contador)
        contador = contador + 1
    return acumulador[posicao - 1]