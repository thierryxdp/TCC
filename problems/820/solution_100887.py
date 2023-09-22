def posLetra(string, letra, num):

    letras = []
    i = 0
    while i < len(string):
        letras.append(string[i])
        i += 1

    counter = 1
    incidencia = 0

    while counter < len(string):
        if letras[counter-1] == letra:
            incidencia += 1
            if incidencia == num:
            return counter
        counter += 1

    return -1