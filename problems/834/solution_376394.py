def media_matriz(matriz):
  	acumulador=0
    contador=0
    linha=len(matriz)
    coluna=len(matriz[0])
    for i in range(linha):
        for j in range(coluna):
            if matriz[i][j]==numero:
                acumulador=acumulador+1
            contador=contador+1
    return round(acumualador/contador,2)