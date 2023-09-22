def pontos_por_time(listaX):
    '''função que recebe uma lista de dois jogos entre dois times
    e retorna a pontuação final de cada time, a entrada tambem
    deve ser definida por duas listas distintas'''
    jogoida = listaX[0]
    jogovolta = listaX[1]
    time1 = jogoida[0]
    time2 = jogoida[1]
    placar1 = jogoida[2]
    placar2 = jogovolta[2]
    pontostime1jogo1 = placar1[0]
    pontostime2jogo1 = placar1[1]
    pontostime1jogo2 = placar2[1]
    pontostime2jogo2 = placar2[0]
    if pontostime1jogo1 > pontostime2jogo1:
        pontuacaot1 = 3
        pontuacaot2 = 0
    elif pontostime1jogo1 < pontostime2jogo1:
        pontuacaot1 = 0
        pontuacaot2 = 3
    elif pontostime1jogo1 == pontostime2jogo1:
        pontuacaot1 = 1
        pontuacaot2 = 1
if pontostime1jogo2 > pontostime2jogo2:
        pontuacaot1 = pontuacaot1 + 3
        pontuacaot2 = pontuacaot2 + 0
    elif pontostime1jogo2 < pontostime2jogo2:
        pontuacaot1 = pontuacaot1 + 0
        pontuacaot2 = pontuacaot2 + 3
    elif pontostime1jogo2 == pontostime2jogo2:
        pontuacaot1 = pontuacaot1 + 1
        pontuacaot2 = pontuacaot2 + 1
    return {time1:pontuacaot1 , time2:pontuacaot2}