#Questão pontos por time
#Função que calcula a pontuação de um time no campeonato
#placar1(jogo de ida([a,b[x,y]]), placar2([b,a[s,t]])jogo de volta)
#lista;lista->dicionário
def pontos_por_time(placar1,placar2):
    """Função que calcula a pontuação de dois times após um jogo de ida e volta"""
    """lista,lista->dicionário"""
    if placar1[2][1]>placar1[2][2] and placar2[2][2]>placar2[2][1]:
        return {placar1[1]:0,placar1[0]:6}
    elif placar1[2][1]<placar1[2][2] and placar2[2][2]<placar2[2][1]:
        return {placar1[1]:6,placar1[0]:0}
    elif placar1[2][1]==placar1[2][2] and placar2[2][2]>placar2[2][1]:
        return {placar1[1]:1,placar1[0]:4}
    elif placar1[2][1]>placar1[2][2] and placar2[2][2]==placar2[2][1]:
        return {placar1[1]:1,placar1[0]:4}
    elif placar1[2][1]==placar1[2][2] and placar2[2][2]<placar2[2][1]:
        return {placar1[1]:4,placar1[0]:1}
    elif placar1[2][1]>placar1[2][2] and placar2[2][2]==placar2[2][1]:
        return {placar1[1]:4,placar1[0]:1}