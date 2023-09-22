def posLetra(string,letra,posicao):
    string = list(string)
    if string[posicao] == letra:
            return string.index(letra)
    else:
        return -1