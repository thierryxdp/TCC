#Start your python function h
def pontos_por_time(jogos):
    jogoida = jogos[0]
    jogovolta = jogos[1]
    time1 = jogoida[0]
    time2 = jogoida[1]
    pontos1 = jogoida[2][0] + jogovolta[2][1]
    pontos2 = jogoida[2][1] + jogovolta[2][0]
    pontos1 = 0
    pontos2 = 0
    if jogoida[2][0] > jogoida [2][1]:
        pontos1 = pontos1 + 3
    elif jogoida[2][0] == jogoida[2][1]:
        pontos1 = pontos1 + 1
        pontos2 = pontos2 + 1
    else:
        pontos2 = pontos2 + 3
    if jogovolta[2][1] > jogovolta[2][0]:
        pontos1 = pontos1 + 3
    elif jogovolta[2][0] > jogovolta[2][1]:
        pontos2 = pontos2 + 3
    else:
        pontos1 = pontos1 + 1
        pontos2 = pontos2 + 1
    if pontos1 > pontos2:
        tabela = {time1 : pontos1,
                  time2 : pontos2}
    else:
        tabela = {time2 : pontos2,
                  time1 : pontos1}
    return tabela