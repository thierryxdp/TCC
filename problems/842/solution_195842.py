def pontos_por_time(saldo_das_partidas):
    """Dado o saldo de gols de duas partidas de um torneio entre Cormengo e Flaminthians, retorna 
    a tabela da soma dos resultados (vitória=3 pontos, empate= 1 pontos) dos times:
    list[[time1,time2,[gols cor,gols fla]],[time2,time1,[gols fla,gols cor]]]
    -->dicionario{'Cormengo':pontuação,'Flaminthíans':pontuação}"""
    partida1=saldo_das_partidas[0]
    partida2=saldo_das_partidas[1]
    time1=saldo_das_partidas[0][0]
    time2=saldo_das_partidas[0][1]
    time1_pontos=[partida1[2][0],partida2[2][1]]
    time2_pontos=[partida1[2][1],partida2[2][0]]
    if time1_pontos[0]>time2_pontos[0] and time1_pontos[1]>time2_pontos[1]:
        return {time1:6,time2:0}
    if time1_pontos[0]>time2_pontos[0] and time1_pontos[1]<time2_pontos[1]:
        return {time1:3,time2:3}
    elif time1_pontos[0]>time2_pontos[0] and time1_pontos[1]==time2_pontos[1]:
        return {time1:4,time2:1}
    elif time1_pontos[0]==time2_pontos[0] and time1_pontos[1]==time2_pontos[1]:
        return {time1:2,time2:2}
    if time1_pontos[0]<time2_pontos[0] and time1_pontos[1]>time2_pontos[1]:
        return {time1:3,time2:3}
    elif time1_pontos[0]<time2_pontos[0] and time1_pontos[1]==time2_pontos[1]:
        return {time1:1,time2:4}
    elif time1_pontos[0]<time2_pontos[0] and time1_pontos[1]<time2_pontos[1]:
        return {time1:0,time2:6}
    else:
        return ""