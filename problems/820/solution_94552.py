def posLetra(frase, letra, n):
    i = i2 = 0
    while i < len(frase):
        if frase.count(letra) < n:
            return -1
        if frase[i] == letra:
            i2 += 1
            if i == n:
                return i
        i += 1