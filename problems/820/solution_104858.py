def posLetra(string,letra,posicao):
    string = list(string)
    i = 0
    index = []
    while i < len(string):
        if string[i] == letra:
            index.append(i)
            i += 1
        if string[i] != letra:
            i += 1
    if max(index) == posicao:
        return max(index)
    if max(index) != posicao:
        return -1