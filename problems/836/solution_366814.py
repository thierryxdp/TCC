def busca(setor, matriz):
    
    numTotalLinhas = len(matriz)
    linha = 0
    saida = []
    while (linha < numTotalLinhas):
        if matriz[linha][2] == setor:
            saida.append(matriz[linha][0])
            saida.append(matriz[linha][1])
            saida.append(matriz[linha][3])
        linha += 1
        
  
    return saida