def posLetra(string, letra, num):
    #str > int
    pos = string.find(letra)
    while pos >= 0 and num > 1:
        pos = string.find(letra, pos + 1)
        num -= 1
    return pos