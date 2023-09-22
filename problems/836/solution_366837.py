def busca(setor, matriz):
    
    numTotalLinhas = len(matriz)
    linha = 0
    saida = []
    matriz2 = []
    numLinha = 0
    while (linha < numTotalLinhas):
        if matriz[linha][2] == setor:
            saida.append(matriz[linha][0])
            saida.append(matriz[linha][1])
            saida.append(matriz[linha][3])
            list.append(matriz2, saida)

        linha += 1

    return matriz2