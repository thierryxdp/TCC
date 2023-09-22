def posLetra(frase, letra, vezes):
    i = 0

    for aux in range(frase):
        if frase[aux] == letra:
            if i == vezes:
                return aux
            else :
                i += 1

    return -1