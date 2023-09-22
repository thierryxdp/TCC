#Start your python function here
def pontos_por_time (jogo_da_ida, jogo_da_volta):
    '''
    	Calcula a pontuação de acordo com o resultado do jogo.
        Parâmetro 1: list
        Parâmetro 2: list
        Resultado: dicionario
    '''
    time1 = jogo_da_ida[0]
    time2 = jogo_da_ida[1]
    resultado1 = jogo_da_ida[2]
    resultado2 = jogo_da_volta[2]
    gol_time1_jogo1 = resultado1[0]
    gol_time2_jogo1 = resultado1[1]
    gol_time1_jogo2 = resultado1[1]
    gol_time2_jogo2 = resultado1[0]
    if gol_time1_jogo1 > gol_time2_jogo1:
        pontos_time1 = 3
        pontos_time2 = 0
    elif gol_time1_jogo1 == gol_time2_jogo1:
        pontos_time1 = 1
        pontos_time2 = 1
    else:
        pontos_time1 = 0
        pontos_time2 = 3
    if gol_time1_jogo2 > gol_time2_jogo2:
        pontos_time1 = pontos_time1 + 3
        pontos_time2 = pontos_time2 + 0
    elif gol_time1_jogo2 == gol_time2_jogo2:
        pontos_time1 = pontos_time1 + 1
        pontos_time2 = pontos_time2 + 1
    else:
        pontos_time1 = pontos_time1 + 0
        pontos_time2 = pontos_time2 + 3
    times = [time1, time2]
    pontos = [pontos_time1, pontos_time2]
    pontuacao_final = dict(zip(times, pontos)
    return pontuacao_final