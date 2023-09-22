def posLetra(string,letra,posicao):
    string = list(string)
    for i in range(len(string)):
        if string[i] == letra:
            return posicao
    else:
        return -1