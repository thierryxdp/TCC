def posLetra(string,letra,posicao):
    string = list(string)
    if string[posicao] == letra:
            return posicao
    else:
        return -1