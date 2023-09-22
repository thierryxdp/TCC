def conta_numero(numero, matriz):
    ''''''
    resultado = 0
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            if numero ==matriz[i][j]:
                resultado+=matriz.count(numero)
            else:
                pass
    return resultado