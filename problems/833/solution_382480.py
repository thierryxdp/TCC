def conta_numero(numero,matriz):
    acumulador=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in linha:
        for i in coluna:
            if i==numero:
                acumulador=acumulador+1
    return acumulador