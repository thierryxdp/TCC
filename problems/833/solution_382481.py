def conta_numero(numero,matriz):
    acumulador=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for i in range(coluna):
            if i==numero:
                acumulador=acumulador+1
    return acumulador