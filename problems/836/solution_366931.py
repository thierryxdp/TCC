def busca(setor, matriz):
    
    numTotalLinhas = len(matriz)
    linha = 0
    saida = []
    matriz2 = []
    numLinha = 0
    for i in range(len(matriz)):
        if matriz[i][2] == setor:
            saida.append(matriz[linha][0])
            saida.append(matriz[linha][1])
            saida.append(matriz[linha][3])
            #matriz2 += [saida]

       #   linha += 1

    return saida