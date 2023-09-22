def posLetra(string, letra, n):
    pos = string.find(letra)
    while pos >= 0 and n > 1:
        pos = string.find(letra, pos + 1)
        n -= 1
    return pos