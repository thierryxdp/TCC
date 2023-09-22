def pontos_por_time(ls):
    """
    Recebe uma lista com duas listas, contendo o jogo de ida e o jogo de volta, junto com o total de gols no jogo de cada time.
    Ls -> Dicionário
    """

    NomeT1 = ls[0][0]
    GolsT1J1 = int(ls[0][2][0])
    NomeT2 = ls[0][1]
    GolsT2J1 = int(ls[0][2][1])
    GolsT1J2 = int(ls[1][2][1])
    GolsT2J2 = int(ls[1][2][0])


    #A primeira partida
    if GolsT1J1 > GolsT2J1:
        PontosT1, PontosT2 = 3, 0

    elif GolsT1J1 == GolsT2J1:
        PontosT1, PontosT2 = 1, 1

    else:
        PontosT1, PontosT2 = 0, 3

    #A segunda partida
    if GolsT1J2 > GolsT2J2:
        PontosT1 += 3

    elif GolsT1J2 == GolsT2J2:
        PontosT1 += 1
        PontosT2 += 1

    else:
        PontosT2 += 3


    Dic = {
        NomeT1 : PontosT1,
        NomeT2 : PontosT2
    }

    return Dic

    #Caso teste pontos_por_time([['Cormengo', 'Flamínthias', [1, 0]], ['Flamínthias', 'Cormengo', [2, 2]]]) -> {'Cormengo': 4, 'Flamínthias': 1}
    #Caso teste pontos_por_time([['Cormengo', 'Flamínthias', [1, 1]], ['Flamínthias', 'Cormengo', [2, 2]]]) -> {'Cormengo': 2, 'Flamínthias': 2}
    #Caso teste pontos_por_time([['Cormengo', 'Flamínthias', [0, 1]], ['Flamínthias', 'Cormengo', [1, 0]]]) -> {'Cormengo': 0, 'Flamínthias': 6}