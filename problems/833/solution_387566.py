def conta_numero(numero,matriz):
    repete = 0
    if len(matriz) == 0:
        return repete
    for i in range(0,len(matriz)):
        if numero in matriz[i]:
            repete = list.count(matriz[i],numero)
    return repete