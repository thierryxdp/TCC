conta_numero(numero,matriz):
    repetidor = 0
    if len (matriz) == 0:
        return repetidor
    for l in range (0, len(matriz)):
        if numero in matriz [l]:
            repetidor += list.count(matriz[l], numero)
            return repetidor