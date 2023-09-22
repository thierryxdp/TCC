def conta_numero(numero,matriz):
    for i in range(0,len(matriz)):
        if numero in matriz[i]:
            repete = list.count(matriz[i],numero)
    return repete