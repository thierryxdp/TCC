#Start your python function h
def pontos_por_time(jogoida, jogovolta):
    time1 = jogoida[0][0]
    time2 = jogoida[0][1]
    pontos1 = jogoida[1][0] + jogovolta[1][1]
    pontos2 = jogoida[1][1] + jogovolta [1][0]
    tabela = {time1 : pontos1,
              time2 : pontos2}
    return tabela