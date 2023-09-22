def posLetra(string, letra, numero):
    pos = string.find(letra)
    while pos >= 0 and numero > 1:
        pos = string.find(letra, pos + 1)
        numero -= 1
    return pos