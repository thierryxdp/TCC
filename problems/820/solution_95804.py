def posLetra(frase, letra, vezes):
    i = 0
    aux = o
    while aux < len(frase):
        if frase[aux] == letra:
            if i == vezes:
                return aux
            else :
                i += 1

    return -1