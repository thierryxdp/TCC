def posLetra(frase, letra, n):
    i = 0
    for caracter in frase:
        if caracter == letra:
            i += 1
        if i == n:
    		return i
    return -1