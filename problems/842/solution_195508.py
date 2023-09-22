def pontos_por_time(lista):
    """Função que recebe uma lista de dois elementos, com as informações: 
    nomes e números de gols de dois times em duas partidas de futebol, no 
    formato, [['Cormengo','Flamínthians',[1,0]]. A função retorna o nome
    do time e o número total de pontos que ele fez na fase.
    list,list->list
    """
    Pontos1 = 0
    Pontos2 = 0
    #Times
    time1 = lista[0][0] = lista[1][1]
    time2 = lista[0][1] = lista[1][0]
    #Placar do jogo de ída
    time1_placar = lista[0][2][0]
    time2_placar = lista[1][2][0]
    #Placar do segundo jogo 
    time1_placar2 = lista[1][2][1]
    time2_placar2 = lista[1][2][0]
    # Resultado do jogo de ída
    if time1_placar > time2_placar:
        Pontos1 = Pontos1 + 3
    if time1_placar < time2_placar:
        Pontos2 = Pontos2 + 3
    if time1_placar == time2_placar:
        Pontos1 = Pontos1 + 1
        Pontos2 = Pontos2 + 1
    # Resultado do jogo de volta
    if time2_placar2 > time1_placar2:
        Pontos1 = Pontos1 + 3
    if time2_placar2 < time1_placar2:
        Pontos2 = Pontos2 + 3
    if time1_placar2 == time2_placar2:
        Pontos1 = Pontos1 + 1
        Pontos2 = Pontos2 + 1
    pontos={time1:Pontos1,time2:Pontos2}
    return pontos