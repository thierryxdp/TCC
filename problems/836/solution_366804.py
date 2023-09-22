def busca(setor, matriz):
    
    numTotalLinhas = len(matriz)
    linha = 0
    while (linha < numTotalLinhas):
        if matriz[linha][2] == setor:
            saida = matriz[linha]
        linha += 1
        
  
    return saida