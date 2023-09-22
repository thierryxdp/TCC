def inverte(frase)
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase