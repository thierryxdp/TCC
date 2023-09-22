def pontos_por_time(listaX):
    """Recebe uma lista de dois elementos, onde cada elemento é tambem uma lista. A lista completa tem informações do númer de gols em dois jogos de futebol entre dois times(joga da ida e jogo da volta) e retorna um dicionário cujos mapeamentos são:nome do time:número total de pontos da fase.
    Os pontos de um time na fase são calculados através de uma soma de pontos, onde vitórias valem 3, empates 1 e derrotas nenhum. O total de pontos da fase é a soma de pontos dos dois jogos da fase
    list->dict"""
    jogoIda = listaX[0]
    jogoVolta = listaX[1]
    time1 = jogoIda[0]
    time2 = jogoIda[1]
    placar1 = jogoIda[2]
    placar2 = jogoVolta[2]
    pontosTime1JG1 = placar1[0]
    pontosTime2JG1 = placar1[1]
    pontosTime1JG2 = placar2[1]
    pontosTime2JG2 = placar2[0]
    if pontosTime1JG1 > pontosTime2JG1:
        pontuacaoT1 = 3
        pontuacaoT2 = 0
    elif pontosTime1JG1 < pontosTime2JG1:
        pontuacaoT1 = 0
        pontuacaoT2 = 3
    elif pontosTime1JG1 == pontosTime2JG1:
        pontuacaoT1 = 1
        pontuacaoT2 = 1
    if pontosTime1JG2 > pontosTime2JG2:
        pontuacaoT1 = pontuacaoT1 + 3
        pontuacaoT2 = pontuacaoT2 + 0
    elif pontosTime1JG2 < pontosTime2JG2:
        pontuacaoT1 = pontuacaoT1 + 0
        pontuacaoT2 = pontuacaoT2 + 3
    elif pontosTime1JG2 == pontosTime2JG2:
        pontuacaoT1 = pontuacaoT1 + 1
        pontuacaoT2 = pontuacaoT2 + 1
    return {time1:pontuacaoT1 , time2:pontuacaoT2}