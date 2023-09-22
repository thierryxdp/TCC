def conta_numero(numero,matriz):
    if len(matriz) == 0:
        return 0
    for i in range(0,len(matriz)):
        if numero in matriz[i]:
            repete += list.count(matriz[i],numero)
    return repete