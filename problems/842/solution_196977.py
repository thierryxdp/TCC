#Start your python function h
def pontos_por_time(jogos):
    jogoida = jogos[0]
    jogovolta = jogos[1]
    time1 = jogoida[0]
    time2 = jogoida[1]
    pontos1 = jogoida[2][0] + jogovolta[2][1]
    pontos2 = jogoida[2][1] + jogovolta[2][0]
    tabela = {time1 : pontos1,
              time2 : pontos2}
    return tabela