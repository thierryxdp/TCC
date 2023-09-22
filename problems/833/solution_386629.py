def conta_numero(numero,matriz):
    qtd = 0
    indice = 0
    for lista in matriz:
        if numero in matriz[indice]:
            qtd += list.count(matriz[indice],numero)
            indice += 1
        else :
            indice += 1
    return qtd