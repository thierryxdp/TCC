def inverte(frase):
    inv = str.split(frase)
    inv.reverse()
    frase = str.join(" ", inv)
    return frase