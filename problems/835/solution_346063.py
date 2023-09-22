def melhor_volta(matriz):
    """ retorna media dos elementos da matriz """
    numVolta = 1
    linha = 0
    corredor = 1
    menorTempo = matriz[0][0]
    #linha += 1
    
    # percorre todas as linhas
    while (linha < 6):
        #percorre a linha
        posicao = 0
        for i in matriz[linha]:
            if i < menorTempo:
                menorTempo = i
                corredor = linha
                numVolta = posicao
            posicao += 1
        linha += 1
    return (corredor, menorTempo, numVolta)