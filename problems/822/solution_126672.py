def repetidos(listaNum):
    repetidos = 0
    i = 1
    while i < len(listaNum):
        numero = listaNum[i]
        numAnt = listaNum[i - 1]
        if numero == numAnt:
            repetidos += 1
        i += 1
    return repetidos