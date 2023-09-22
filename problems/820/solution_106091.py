def posLetra(string, letra, num):
    pos = string.index(letra)
    while pos >= 0 and num > 1:
        pos = string.index(letra, pos + 1)
        num -= 1
    return pos