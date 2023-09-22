def posLetra(frases, letra, n):
    pos = frases.find(letra)
    while pos >= 0 and n > 1:
        pos = frases.find(letra, pos + 1)
        n = n - 1
    return pos