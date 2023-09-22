#Start your python function here
def pontos_por_time (lista1, lista2):
    '''
    	Calcula a pontuação de acordo com o resultado do jogo.
        Parâmetro 1: list
        Parâmetro 2: list
        Resultado: dicionario
    '''
    time1 = lista1[0]
    time2 = lista1[1]
    resultado1 = lista1[2]
    resultado2 = lista2[2]
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
    pontuacao_final = [str(time1) : pontos_time1, str(time2) : pontos_time2]
    return pontuacao_final