def posLetra(frase, letra, n):
    i = 0
    u = 0
    while u < len(frase):
        if frase[u] == letra:
            i += 1
        if i == n:
    		return frase.index(letra, u)
        u += 1
    return -1