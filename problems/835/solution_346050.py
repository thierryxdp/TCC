def melhor_volta(matriz):
    """ retorna media dos elementos da matriz """
    menorTempo = 0
    numVolta = 0

    numElementos = len(matriz) * len(matriz[0])
    linha = 0
    numTotalLinhas = len(matriz)
    
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
                volta = posicao
            posicao += 1
        linha += 1
    return (corredor, menorTempo, volta)
    return round(media, 2)