def melhor_volta(matriz):
    """
    função que entrega o melhor tempo de uma volta, de qual corredor, e em qual volta foi.
    list -> tuple 
    """

    tempos = []

    #Salva todos os melhores tempos dos corredores e em qual volta foi a melhor
    for i in range(len(matriz)):
        corredor = []
        for j in range(len(matriz[i])):
            if j == 0:
                corredor.append((matriz[i][j], j)) #Salva uma tupla com o valor do tempo e a volta porque é a primeira
            else:
                while j < len(matriz):
                    if matriz[i][j] > matriz[i][(j-1)]:
                        corredor.clear()
                        corredor.append((matriz[i][j], j))
        tempos.append(corredor)

    melhor = tempos[0]

    #Vê quem foi o melhor no geral da lista de tuplas salvas
    for i in range(len(tempos)):
        if tempos[i][0] > melhor[0]:
            melhor = tempos[i]
    
    return melhor