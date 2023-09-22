def melhor_volta(matriz:list)->tuple:

    """ Função que recebe uma matriz 6x10 com o tempo e a rodade de seis corredores
        de Kart em 10 voltas. A função retorna de quem foi a melhor volta da prova,
        com qual tempo e em que volta.

    """

    melhor_individual = []
    melhor_rodada = []

    for i in range(len(matriz)):


        for n in range(len(matriz)):

            list.append(melhor_individual,matriz[i][n])

        list.append(melhor_rodada,max(melhor_individual))

    melhor_pontuacao = max(melhor_rodada)


    for j in range(len(matriz)):


        for k in range(len(matriz)):

            if matriz[j][k] == melhor_pontuacao:

                jogador = j
                rodada = k


    return(jogador,melhor_pontuacao,rodada)