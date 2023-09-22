def posLetra(string,letra,numero):
    i = 0
    i2 = 0
    if string.count(letra) < numero:
        return -1
    while i2 < numero:
        if string[i] == letra:
            i2 = i2 + 1
        i = i + 1
    return i-1