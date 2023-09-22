def posLetra(string, letra, numero):
    i = 0
    n = 0
    while i < len(string):
        if string[i] = letra:
            n = n + 1
        if n = numero:
            return i
        i = i + 1
    return -1