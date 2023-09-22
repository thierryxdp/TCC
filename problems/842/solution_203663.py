def pontos_por_time(listaDaFase):
    '''Calcula a pontuação de dois times em uma fase com jogos 
    de ida e de volta. Forneça a lista da fase no modelo:
    [['time1','time2',[golsT1,golsT2]], ['time2','time1',[golsT2,golsT1]]].
    list --> dict'''
    jogoIda = listaDaFase[0]
    jogoVolta = listaDaFase[1]
    time1 = jogoIda[0]
    time2 = jogoIda[1]
    placarT1xT2 = jogoIda[2]
    golsT1_JG1 = placarT1xT2[0]
    golsT2_JG1 = placarT1xT2[1]
    placarT2xT1 = jogoVolta[2]
    golsT1_JG2 = placarT2xT1[1]
    golsT2_JG2 = placarT2xT1[0]
    if golsT1_JG1 > golsT2_JG1:
        pontosT1 = 3
        pontosT2 = 0
    if golsT1_JG1 < golsT2_JG1:
        pontosT1 = 0
        pontosT2 = 3
    if golsT1_JG1 == golsT2_JG1:
        pontosT1 = 1
        pontosT2 = 1
    if golsT1_JG2 > golsT2_JG2:
        pontosT1 = pontosT1 + 3
        pontosT2 = pontosT2 + 0
    if golsT1_JG2 < golsT2_JG2:
        pontosT1 = pontosT1 + 0
        pontosT2 = pontosT2 + 3
    if golsT1_JG2 == golsT2_JG2:
        pontosT1 = pontosT1 + 1
        pontosT2 = pontosT2 + 1
    return {time1:pontosT1,time2:pontosT2}