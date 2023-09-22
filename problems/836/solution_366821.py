def busca(setor, matriz):
    
    numTotalLinhas = len(matriz)
    linha = 0
    saida = []
    matriz = []
    numLinha = 0
    while (linha < numTotalLinhas):
        if matriz[linha][2] == setor:
            saida.append(matriz[linha][0])
            saida.append(matriz[linha][1])
            saida.append(matriz[linha][3])
            matriz.append(saida)

        linha += 1
  
    return matriz