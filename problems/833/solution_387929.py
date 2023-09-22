conta_numero(numero,matriz):
    repetidor=0
    if len (matriz)==0:
        return repetidor
    for l in range (0, len(matriz)):
        if numero in matriz [1]:
            repetidor += list.count(matriz[1],numero)
    return repetidor