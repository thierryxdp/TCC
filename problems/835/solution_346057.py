def melhor_volta(matriz):
    """ retorna media dos elementos da matriz """
    menorTempo = 0
    numVolta = 0
    linha = 0
    numTotalLinhas = len(matriz)
    corredor = 0
    menorTempo = min(matriz[linha])
    linha += 1
    
    # percorre todas as linhas
    while (linha < numTotalLinhas):
        #percorre a linha
        posicao = 0
        for i in matriz[linha]:
            if menorTempo > i:
                menorTempo = i
                corredor = linha
                numVolta = posicao
            posicao += 1
        linha += 1
    return (corredor, menorTempo, numVolta)