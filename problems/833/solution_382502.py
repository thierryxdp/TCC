def conta_numero(numero,matriz):
    """Retorna quantas vezes o numero aparece na matriz.
    Parametros:
    Entrada:int,list
    Saida:int"""
    acumulador=0
    if matriz==[]:
        return acumulador
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j]==numero:
                acumulador=acumulador+1
    return acumulador