def melhor_volta(matriz:list)->tuple:

    """ Função que recebe uma matriz 6x10 com o tempo e a rodade de seis corredores
        de Kart em 10 voltas. A função retorna de quem foi a melhor volta da prova,
        com qual tempo e em que volta.

    """

    total = []

    for i in range(6):

        for n in range(10):

            list.append(total,matriz[i][n])
            
    melhor_pontuacao = min(total)

    for j in range(6):

        for k in range(10):

            if matriz[j][k] == melhor_pontuacao:

                jogador = j
                rodada = k


    return(jogador,melhor_pontuacao,rodada)