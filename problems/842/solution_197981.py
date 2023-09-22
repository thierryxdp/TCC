def pontos_por_time(jogos):
    """Define uma lista que recebe duas listas referentes a pontuação dos times e retorna o time e seus pontos """
    jogoida = jogos[0]
    jogovolta = jogos[1]
    time1 = jogoida[0]
    time2 = jogoida[1]
    pontos1 = jogoida[2][0]+jogovolta[2][1]
    pontos2 = jogoida[2][1]+jogovolta[2][0]
    pontos1 = 0
    pontos2 = 0
    if  jogoida[2][0]>jogoida[2][1]:
        pontos1 = pontos1+3
    elif jogoida[2][0]==jogoida[2][1]:
        pontos1 = pontos1+1
        pontos2 = pontos2+2
    else:
        pontos2 = pontos2+3
    if jogovolta[2][1]>jogovolta[2][0]:
        pontos1 = pontos1+3
    elif jogovolta[2][0]>jogovolta[2][1]:
        pontos2= pontos2+3
    else:
        pontos1=pontos1+1
        pontos2=pontos2+2
    tabela={time1:pontos1,time2:pontos2}
    return tabela