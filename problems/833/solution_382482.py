def conta_numero(numero,matriz):
    acumulador=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if matriz[j][i]==numero:
                acumulador=acumulador+1
    return acumulador