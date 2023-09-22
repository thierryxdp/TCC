def posLetra(frase, letra, n):
    i = 0
    contador = 0
    while i < len(frase):
        if frase[i] == letra:
            contador = contador + 1
            if contador == n:
                if i == None:
                    return -1
                else:
                    return i
        i = i + 1