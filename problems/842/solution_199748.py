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
    if resultado1[0] > resultado1[1]:
        pontos_time1 = 3
        pontos_time2 = 0
    elif resultado1[0] == resultado1[1]:
        pontos_time1 = 1
        pontos_time2 = 1
    else:
        pontos_time1 = 0
        pontos_time2 = 3
    if resultado2[0] > resultado2[1]:
        pontos_time1 = pontos_time1 + 0
        pontos_time2 = pontos_time2 + 3
    elif resultado2[0] == resultado2[1]:
        pontos_time1 = pontos_time1 + 1
        pontos_time2 = pontos_time2 + 1
    else:
        pontos_time1 = pontos_time1 + 3
        pontos_time2 = pontos_time2 + 0
    pontuacao_final = {time1 : pontos_time1, time2 : pontos_time2}
    return pontuacao_final